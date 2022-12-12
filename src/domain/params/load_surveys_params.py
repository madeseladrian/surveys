from typing import List, TypedDict
from ..models import SurveyModel


class LoadSurveysResult(TypedDict):
    list: List[SurveyModel]
