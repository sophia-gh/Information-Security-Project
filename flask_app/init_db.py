import sqlite3

#creates a connection to a database file which will be created after running this python file
connection = sqlite3.connect('database.db')

#opens schema file and executes the sql commands, creates user table
with open('databaseSchema.sql') as f:
    connection.executescript(f.read())

#used to interact with the rows of the database table
cur = connection.cursor() 

#populate users with data
cur.execute("INSERT INTO users (user_name, email, password) VALUES(?, ?, ?)", ('johndoe', 'john@example.com', 'supersecret'))
cur.execute("INSERT INTO users (user_name, email, password) VALUES(?, ?, ?)", ('test1', 'test1@example.com', 'password1'))
cur.execute("INSERT INTO users (user_name, email, password) VALUES(?, ?, ?)", ('test2', 'test2@example.com', 'password2'))
cur.execute("INSERT INTO users (user_name, email, password) VALUES(?, ?, ?)", ('test3', 'test3@example.com', 'password3'))


connection.commit()
connection.close()
