import json

from auth.login import login
from evidences.authenticated_user_evidence import collect_user_details_using_token
from evidences.collect_posts import collect_posts, collects_posts_with_comments

with open("dummy_db.json") as f:
    db = json.load(f)

def collect_all_evidences():
    token = login_with_valid_credentials()
    user_details = collect_user_details_using_token(token)
    posts = collect_posts()
    posts_with_comments = collects_posts_with_comments()
    print(user_details)
    print(posts)
    print(posts_with_comments)


def login_with_valid_credentials():
    valid_credentials = db["valid_credentials"][0]
    token = login(valid_credentials)
    return token

print(collect_all_evidences())
