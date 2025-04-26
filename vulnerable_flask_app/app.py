import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash  # for password hashing
from flask import Flask, render_template, request, url_for, flash, redirect, session
from encryption import global_key, AES_ENCRYPT, AES_DECRYPT # for encrypting user emails

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devKeyForDEV'

def get_db_connection():
    conn = sqlite3.connect('vulnerable_database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    # fetch data from the database and display it on the index page
    conn = get_db_connection()
    try: all_users = conn.execute('SELECT * FROM users').fetchall()
    except (sqlite3.OperationalError) as e:
        return f"[Database Error: {str(e)}]"  # if there is no table to display, error will be displayed instead
    conn.close()
    # create seperate list of users to pass to the index.html for display
    # for logged in user, decrypts email to show plain text email on the page to demonstrate successful decryption
    decrypted_users = []
    for user in all_users:
        user_dict = dict(user)
        user_dict['user_name'] = user['user_name']  
        user_dict['password'] = generate_password_hash(user['password']) # for displaying purposes, shows hashed password instead of the stored plain text in the vulnerable database
        if user and (user['user_name'] == session.get('username')):     #if a user is logged in, show that user's decrypted email
            user_dict['email'] = AES_DECRYPT(user['email'], user['AES_key'])
        else:
            user_dict['email'] = user['email']
        decrypted_users.append(user_dict)

    return render_template('index.html', all_users=decrypted_users)

@app.route('/create_account', methods=['GET', 'POST'])       #get and post methods allow both fetching and adding to the database
def create_account():
    # simple html form to submit user information 
    if request.method == 'POST':
        # set up some variables to get from the html form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # simple input error handling 
        if not username or not email or not password:
            flash('Please fill out all fields!')
            return redirect(url_for('create_account'))
        
        # check for existence of info before attempting insertion
        conn = get_db_connection()
        user_exists = conn.execute('SELECT * FROM users WHERE user_name = ?', (username,)).fetchone()

        #encrypt email first to check correctly
        encrypted_email = AES_ENCRYPT(email, global_key)
        email_exists = conn.execute('SELECT * FROM users WHERE email = ?', (encrypted_email,)).fetchone()
        
        # simple input error handling 
        if user_exists:
            flash('Username already exists. Try another one.')
            conn.close()
            return redirect(url_for('create_account'))
        if email_exists:
            flash('Account already exits for this email. Try another one.')
            conn.close()
            return redirect(url_for('create_account'))
       
        # now attempting insertion
        # for vulnerable version, in order for sql injection attacks to work, store password as plaintext in the database instead of hashed
        user = conn.execute("INSERT INTO users (user_name, email, password, AES_key) VALUES(?, ?, ?, ?)", (username, encrypted_email, password, global_key))
        conn.commit()
        conn.close()
        if user:
            session['username'] = username
            flash('Account created successfully!')
            return redirect(url_for('index'))
    return render_template('create_account.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # simple html form to login a user
    if request.method == 'POST':
        # set up variables
        username = request.form['username']
        password = request.form['password']
        
        # simple error handling 
        if not username or not password:
            flash('Please fill out all fields!')
            return redirect(url_for('login'))
        
        #----------------------------------------------------------------------------------------------------------------------------
        # query structured to be vulnerable to injection -- no paramaterization
        # attack example: user can enter a malicious string for 'username' or 'password'
        #             ex: username = ('OR 1=1 --) this would log attacker in as first available user 
        #             ex: stacked queries such as-- username = ('OR 1=1; DROP TABLE users --) 
        #                 this would allow an attacker to drop users from the database
        conn = get_db_connection()
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE user_name = '{username}' and password = '{password}'" # sql injection attack only possible if the password is stored as plain text in the database
        user = cursor.execute(query).fetchone() # to demonstrate malicious login
        #user = cursor.executescript(query).fetchone() # to demonstrate stacked queries, great for vulnerable app -- bad otherwise
        conn.close()
        #----------------------------------------------------------------------------------------------------------------------------
        # checks if user is populated, now sets session to username from database, not from input, so an attacker could log in and 
        # removed check password hash because there is no way to structure this so its vulnerable with a hashed password
        # sensitive data
        if user:
            session['username'] = user['user_name']
            flash('Logged in successfully!')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        #----------------------------------------------------------------------------------------------------------------------------
    return render_template('login.html')

@app.route('/logout')
def logout():
    # clear session, return to index page
    session.clear()
    flash('Logged out successfully.')
    return redirect(url_for('index'))

@app.route('/secret_page')
def secret_page():
    return render_template('secret.html')
