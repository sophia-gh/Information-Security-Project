import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash  # for password hashing
# for encrypting emails
from encryption import global_key, AES_ENCRYPT, AES_DECRYPT

#creates a connection to a database file which will be created after running this python file
connection = sqlite3.connect('database.db')

#opens schema file and executes the sql commands, creates user table
with open('databaseSchema.sql') as f:
    connection.executescript(f.read())

#used to interact with the rows of the database table
cur = connection.cursor() 

#populate users with data
cur.execute("INSERT INTO users (user_name, email, password, AES_key) VALUES(?, ?, ?, ?)", ('johndoe', AES_ENCRYPT('john@example.com', global_key), generate_password_hash('supersecret'), global_key))
cur.execute("INSERT INTO users (user_name, email, password, AES_key) VALUES(?, ?, ?, ?)", ('test1',  AES_ENCRYPT('test1@example.com', global_key), generate_password_hash('password1'), global_key))
cur.execute("INSERT INTO users (user_name, email, password, AES_key) VALUES(?, ?, ?, ?)", ('test2', AES_ENCRYPT('test2@example.com', global_key), generate_password_hash('password2'), global_key))
cur.execute("INSERT INTO users (user_name, email, password, AES_key) VALUES(?, ?, ?, ?)", ('test3', AES_ENCRYPT('test3@example.com', global_key), generate_password_hash('password3'), global_key))

connection.commit()
connection.close()
