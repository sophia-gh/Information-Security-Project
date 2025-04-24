import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash  # for password hashing
# for encrypting emails
from encryption import global_key, AES_ENCRYPT, AES_DECRYPT

#creates a connection to a database file which will be created after running this python file
connection = sqlite3.connect('vulnerable_database.db')

#opens schema file and executes the sql commands, creates user table
with open('vdatabaseSchema.sql') as f:
    connection.executescript(f.read())

#used to interact with the rows of the database table
cur = connection.cursor() 

#populate users with data
cur.execute("INSERT INTO users (user_name, email, password) VALUES(?, ?, ?)", ('johndoe', AES_ENCRYPT('john@example.com', global_key), generate_password_hash('supersecret')))
cur.execute("INSERT INTO users (user_name, email, password) VALUES(?, ?, ?)", ('test1',  AES_ENCRYPT('test1@example.com', global_key), generate_password_hash('password1')))
cur.execute("INSERT INTO users (user_name, email, password) VALUES(?, ?, ?)", ('test2', AES_ENCRYPT('test2@example.com', global_key), generate_password_hash('password2')))
cur.execute("INSERT INTO users (user_name, email, password) VALUES(?, ?, ?)", ('test3', AES_ENCRYPT('test3@example.com', global_key), generate_password_hash('password3')))

connection.commit()
connection.close()
