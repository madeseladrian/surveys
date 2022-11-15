from pydantic import BaseModel


class Message(BaseModel):
    detail: str

responses: dict = {
  400: {"model": Message, "description": "BadRequest Error"},
  403: {"model": Message, "description": "Forbidden Error"},
  500: {"model": Message, "description": "Server Error"}
}
