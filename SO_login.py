import os
import requests

payload = {
    'email': os.environ.get('SO_USR'),
    'password': os.environ.get('SO_PWD'),
}

login_url = 'https://stackoverflow.com/users/login'
with requests.Session() as c:
    r = c.post(login_url, data=payload)
    print('martin-martin' in r.text)
