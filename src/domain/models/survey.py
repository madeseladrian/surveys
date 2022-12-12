from datetime import datetime
from typing import List, Optional, TypedDict


class SurveyAnswerModel(TypedDict):
    image: Optional[str]
    answer: str

class SurveyModel(TypedDict):
    id: str
    question: str
    answers: List[SurveyAnswerModel]
    date: datetime
    didAnswer: Optional[bool]
