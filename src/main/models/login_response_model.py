from pydantic import BaseModel


class LoginResponseModel(BaseModel):
    name: str
    access_token: str
    token_type: str
