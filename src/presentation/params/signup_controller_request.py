from typing import TypedDict

class SignUpControllerRequest(TypedDict):
  name: str
  email: str
  password: str
  password_confirmation: str
