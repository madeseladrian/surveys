from typing import TypedDict

class AddAccountRepositoryParams(TypedDict):
    name: str
    email: str
    password: str

AddAccountRepositoryResult = bool
