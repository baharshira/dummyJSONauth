from typing import List
import concurrent.futures

from evidences.base import BaseEvidence
from services.http_client import get
from models.post import Post, Comment
from config.settings import BASE_URL, POSTS_ENDPOINT


class PostEvidence(BaseEvidence):
    def collect(self, token: str = None) -> List[Post]:
        response = get(f"{BASE_URL}{POSTS_ENDPOINT}?limit=60")
        posts_data = response.get("posts", [])
        posts = [Post(**post) for post in posts_data]
        return self._enrich_with_comments(posts)

    def _enrich_with_comments(self, posts: List[Post]) -> List[Post]:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self._fetch_comments, post) for post in posts]
            return [f.result() for f in futures]

    def _fetch_comments(self, post: Post) -> Post:
        comments_url = f"{BASE_URL}{POSTS_ENDPOINT}/{post.id}/comments"
        data = get(comments_url)
        comments = [Comment(**c) for c in data.get("comments", [])]
        post.comments = comments
        return post