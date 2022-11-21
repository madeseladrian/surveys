from pydantic import BaseModel


class Message(BaseModel):
    detail: str

sign_up_responses: dict = {
    400: {"model": Message, "description": "BadRequest Error"},
    403: {"model": Message, "description": "Forbidden Error"},
    500: {"model": Message, "description": "Server Error"}
}
