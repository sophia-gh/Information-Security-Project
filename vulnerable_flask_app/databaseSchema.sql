--create user table
DROP TABLE IF EXISTS users;
CREATE TABLE users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--insert data for testing 
-- INSERT INTO users (user_name, email, password)
-- VALUES ('johndoe', 'john@example.com', 'supersecret');

-- INSERT INTO users (user_name, email, password)
-- VALUES ('test1', 'test1@example.com', 'password1');

-- INSERT INTO users (user_name, email, password)
-- VALUES ('test2', 'test2@example.com', 'password2');

-- INSERT INTO users (user_name, email, password)
-- VALUES ('test3', 'test3@example.com', 'password3');
