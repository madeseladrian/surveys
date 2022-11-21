from typing import TypedDict


class AuthMiddlewareRequest(TypedDict):
    access_token: str
