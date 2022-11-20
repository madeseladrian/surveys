from typing import List, Optional, TypedDict


class Answer(TypedDict):
    image: Optional[str]
    answer: str

class AddSurveyControllerRequest(TypedDict):
    question: str
    answers: List[Answer]
