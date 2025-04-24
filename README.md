# Information-Security-Project
This is a very minimal python flask app that showcases propper sql and database management, as well safe storage of data. For encrypting emails I used a simplified AES(256) implimentation using the 'pycryptodome' library. The implementation in this project is not secure in a production environent as it does not emmploy proper key storage or generation. For password storage I used a simple hash function from the werkzeug library, this was simpler to implement because it was one sided and had less variables to manage. For the front end I used flask to create webpages to interact with the database. The database was implemented and manipulated using sqlite 3. 
## Tutorials and References
>I followed this tutorial for the creating the general strucure of a flask app and connecting it to my database. I diverge from the tutorial in my database structuring and the paged I chose to include. 
>- src: Dyouri, A. (2021a, November 18). How to use an sqlite database in a flask application. DigitalOcean. https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application 

>I followed this tutorial to make the encryption and decryption functions. I diverged from this tutorial for my purposes, especially in the decryption function. 
>- src: Basile. (2022, April 13). AES encryption & decryption in python: Implementation, Modes & Key Management.  Onboardbase. https://onboardbase.com/blog/aes-encryption-decryption/ 

>I also used this page for documentation of pycryptodome.
>- src: Modern modes of operation for symmetric block ciphers. Modern modes of operation for symmetric block ciphers - PyCryptodome 3.230b0 documentation. (n.d.). https://www.pycryptodome.org/srccipher/modern#eax-mode 

How to Run-- For sql error free version navigate to flask-app directory, for sql vulnerable version navigate to vulnerable_flask_app directory

1. install libraries: make sure sqlite3 is already installed 
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
Technoloies Used
> python flask -- python library

> sqlite3 -- downloaded precompiled binaries for windows

> werkzeug -- python library

> pycryptodome -- python library


