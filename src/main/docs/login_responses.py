from pydantic import BaseModel


class Message(BaseModel):
    detail: str

login_responses: dict = {
    400: {"model": Message, "description": "BadRequest Error"},
    401: {"model": Message, "description": "Unauthorized Error"},
    500: {"model": Message, "description": "Server Error"}
}
