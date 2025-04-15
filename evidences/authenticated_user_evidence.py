import requests

from config.settings import  BASE_URL, MY_USER_DETAILS_ENDPOINT

def collect_user_details_using_token(token):
    url = BASE_URL + MY_USER_DETAILS_ENDPOINT
    headers = {
        'Authorization': f'Bearer {token}'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print("Unauthorized: Invalid or expired token.")
        else:
            print(f"Unexpected status {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None






