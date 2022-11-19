from pydantic import BaseModel
from typing import Any

class LoginResponseModel(BaseModel):
    body: Any
