from evidences.base import BaseEvidence
from services.http_client import get
from models.user import UserDetails
from config.settings import BASE_URL, MY_USER_DETAILS_ENDPOINT


class UserEvidence(BaseEvidence):
    def collect(self, token: str):
        url = BASE_URL + MY_USER_DETAILS_ENDPOINT
        headers = {"Authorization": f"Bearer {token}"}
        data = get(url, headers)
        if data:
            return UserDetails(**data)
        return None
