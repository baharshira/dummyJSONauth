from pydantic import BaseModel
from typing import List, Optional


class Comment(BaseModel):
    id: int
    body: str
    postId: int
    user: dict

class Reaction(BaseModel):
    likes: int
    dislikes: int

class Post(BaseModel):
    id: int
    title: str
    body: str
    tags: List[str]
    reactions: Reaction
    comments: Optional[List[Comment]] = []