from typing import TypedDict


class AuthenticationParams(TypedDict):
    email: str
    password: str

class AuthenticationResult(TypedDict):
    access_token: str
    name: str
