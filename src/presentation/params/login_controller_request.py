from typing import TypedDict


class LoginControllerRequest(TypedDict):
    email: str
    password: str
