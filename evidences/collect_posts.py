import requests

from config.settings import BASE_URL, POSTS_ENDPOINT


def collect_posts(limit=60):
    url = f"{BASE_URL}{POSTS_ENDPOINT}"

    if limit is not None:
        url = f"{url}?limit={limit}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("posts", [])
        else:
            print(f"Failed to retrieve posts. Status {response.status_code}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return []

def collects_posts_with_comments():
    posts = collect_posts()
    # I know it's not the best way - should have done it in a single batch. Many API requests will increase the latency!
    # This is a very slow solutin with many API calls, not the fastest and most efficient implementation
    enriched_posts = []

    for post in posts:
        post_id = post["id"]
        comments_url = f"{BASE_URL}{POSTS_ENDPOINT}/{post_id}/comments"

        try:
            response = requests.get(comments_url)
            response.raise_for_status()
            comments = response.json().get("comments", [])
            post["comments"] = comments
        except Exception as e:
            print(f"Unexpected error: {e}")
            post["comments"] = []

        enriched_posts.append(post)

    return enriched_posts