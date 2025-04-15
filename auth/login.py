import json
import requests

from config.settings import BASE_URL, LOGIN_ENDPOINT


def login(credentials):
    url = BASE_URL + LOGIN_ENDPOINT
    headers = {'Content-Type': 'application/json'}

    # In real life scenario I would never write plain passwords in DB!
    # And use a better error handling and a middleware for authentication, and store the token somewhere else (like cookie)
    try:
        response = requests.post(url, headers=headers, data=json.dumps(credentials))
        if response.status_code == 200:
            data = response.json()
            access_token = data.get("accessToken")
            return access_token
        elif response.status_code == 400:
            print(f"Invalid credentials for user: {credentials['username']}")
        elif response.status_code == 401:
            print(f"Unauthorized: Wrong credentials for user {credentials['username']}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None
