# Information-Security-Project
This is a very minimal python flask app that showcases propper sql and database management, as well safe storage of data. For encrypting emails I used a simplified AES(256) implimentation using the 'pycryptodome' library. The implementation in this project is not secure in a production environent as it does not emmploy proper key storage or generation. For password storage I used a simple hash function from the werkzeug library, this was simpler to implement because it was one sided and had less variables to manage. For the front end I used flask to create webpages to interact with the database. The database was implemented and manipulated using sqlite 3. 

### How to Run-- For sql error free version navigate to flask_app directory, for sql vulnerable version navigate to vulnerable_flask_app directory

1. install libraries: make sure sqlite3 is already installed on your computer
```
$ pip install flask
$ pip install werkzeug
$ pip install pycryptodome
```
2. initailize the database
```
$ python init_db.py
```
3. run the app on a local server
```
$ flask --app app run
```
4. open the link provded from running the flask command

### Obstacles and Workarounds
> Secure Version 
>> Encryption: For encryption I used the pycryptodome library which provided functions for implementing AES encryption and decryption, as well as key generation. The problem I ran into was key consitency. To fix this I stored the key used for encryption in an additional column on the user table. And for decryption I accessed the key from user table to maintain consitency. 

#

> Vulnerable Version
>> SQL Injection Vulnerability and Password Hashing: For password Hashing I utilized function from the werkzeug security library. These functions came with their own use cases for the flask app that differ from password checking through SQL only. With hashed passwords, SQL injection was impossible to do through the login portal unless the 'attacker' knew the password of some user in the table. To work around this issue, i decided to store the passwords in the vulnerable version as plain-text instead, and use SQL queries only to login. 

### Tutorials and References
>I followed this tutorial for the creating the general strucure of a flask app and connecting it to my database. I diverge from the tutorial in my database structuring and the pages I chose to include. 
>- src: Dyouri, A. (2021a, November 18). How to use an sqlite database in a flask application. DigitalOcean. https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application 

>I followed this tutorial to make the encryption and decryption functions. I diverged from this tutorial for my purposes, especially in the decryption function. 
>- src: Basile. (2022, April 13). AES encryption & decryption in python: Implementation, Modes & Key Management.  Onboardbase. https://onboardbase.com/blog/aes-encryption-decryption/ 

>I also used this page for documentation of pycryptodome.
>- src: Modern modes of operation for symmetric block ciphers. Modern modes of operation for symmetric block ciphers - PyCryptodome 3.230b0 documentation. (n.d.). https://www.pycryptodome.org/srccipher/modern#eax-mode 

### Technoloies Used
> python flask -- python library

> sqlite3 -- downloaded precompiled binaries for windows

> werkzeug -- python library

> pycryptodome -- python library

