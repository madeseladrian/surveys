from dataclasses import dataclass

from ...domain.features import AddSurvey
from ...domain.params import AddSurveyParams
from ..contracts.db.survey import AddSurveyRepository


@dataclass
class DbAddSurvey(AddSurvey):
    add_survey_repository: AddSurveyRepository

    def add(self, data: AddSurveyParams) -> None:
        self.add_survey_repository.add(data)
