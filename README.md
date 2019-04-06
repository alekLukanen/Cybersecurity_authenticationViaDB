# Authenticate Using a DB
Description of application goes here...


## Build the Development Environment
To create your python environment simply run
```
make build_env
```
from this repositories base directory and then run
```
source env/bin/activate
```
as well. This will activate the virtual environment 
created in the first line of code. All development should
be done using this environment to ensure that results can
be reproduced by other contributors.


## What to Run
Now that you have your virtual environment installed
and activated you can run the server using the following command
```
python auth/manage.py runserver
```


## What Needs to Work

* Login/Register page (index.html)
* Profile page (profile.html)
* Public key cryptography to encrypt username and password
* Admin accounts


## Helpful Curl Commands

| Command | Description
|---      |---
|  curl -X POST http://127.0.0.1:8000/api/users/register/ -H "Content-Type: application/json" -d '{"username": "bob", "email":"bob@example.com", "password":"pass"}' | Create a new user named 'bob' that has password 'pass' |
| curl -X POST -d "grant_type=password&username=<username>&password=<password>" -u "<client_id>:<client_secret>" http://localhost:8000/api/users/o/token/ | Given a username and password authenticate and get a token. |
| curl -X POST -d "grant_type=refresh_token&refresh_token=<refresh_token>" -u "<client_id>:<client_secret>" http://localhost:8000/api/users/o/token/ | Refresh the users access token. |


## Helpful Links

* https://docs.kali.org/general-use/kali-linux-sources-list-repositories
* https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/
* Encrypt and decrypt in python: https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html#Crypto.PublicKey.RSA.RsaKey
* RSA encrypt with PKCS1-V1_5 (Python): https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html
* https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html
* Encrypt and decrypt in javascript: https://medium.com/sharenowtech/high-speed-public-key-cryptography-in-javascript-part-1-3eefb6f91f77
* RSA encrypt with PKCS1-V1_5 (JavaScript): https://stackoverflow.com/questions/46467740/rsa-encrypt-with-pkcs1-v1-5-javascript
* Python and Javascript encryption: https://medium.com/@DannyAziz97/rsa-encryption-with-js-python-7e031cbb66bb
---

