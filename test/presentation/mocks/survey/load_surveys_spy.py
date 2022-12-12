from typing import List

from src.domain.features import LoadSurveys
from src.domain.models import SurveyModel
from src.domain.params import LoadSurveysResult

from ....domain.mocks import mock_survey_models


class LoadSurveysSpy(LoadSurveys):
    account_id: str
    result: List[SurveyModel] = mock_survey_models()

    def load(self, account_id: str) -> LoadSurveysResult:
        self.account_id = account_id
        return self.result
