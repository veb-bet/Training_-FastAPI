from typing import List
from .models import User

users: List[User] = []

def add_user(user: User):
    users.append(user)

def get_all_users() -> List[User]:
    return users
