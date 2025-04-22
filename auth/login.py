import json
import requests

from config.settings import BASE_URL, LOGIN_ENDPOINT


def login(credentials):
    url = BASE_URL + LOGIN_ENDPOINT
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(credentials))
        if response.status_code == 200:
            return response.json().get("accessToken")
        print(f"Login failed: {response.status_code}")
    except Exception as e:
        print(f"Login error: {e}")
    return None