import requests
import json

url = 'https://dummyjson.com/auth/login'
headers = {'Content-Type': 'application/json'}
payload = {
    'username': 'emilys',
    'password': 'emilyspass',
    'expiresInMins': 30
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

# To include cookies in future requests (if needed)
session = requests.Session()
session.cookies.update(response.cookies)

print(response.json())
