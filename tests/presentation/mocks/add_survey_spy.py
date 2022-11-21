from src.domain.features import AddSurvey
from src.domain.params import AddSurveyParams


class AddSurveySpy(AddSurvey):
    params: AddSurveyParams

    def add(self, params: AddSurveyParams) -> None:
        self.params = params
