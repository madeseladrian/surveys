from typing import List, Optional, TypedDict
from datetime import datetime

class SurveyAnswerModel(TypedDict):
    image: Optional[str]
    answer: str

class AddSurveyParams(TypedDict):
    id: Optional[str]
    question: str
    answers: List[SurveyAnswerModel]
    date: datetime
    did_answer: Optional[bool]
