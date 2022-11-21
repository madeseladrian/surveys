from typing import Tuple

from src.domain.features import AddSurvey
from src.domain.params import AddSurveyParams
from src.data.usecases import DbAddSurvey

from ...domain.mocks import mock_add_survey_params
from ..mocks import AddSurveyRepositorySpy


class TestDbAddSurvey:
    # SetUp
    params: AddSurveyParams = mock_add_survey_params()

    SutTypes = Tuple[
        AddSurvey,
        AddSurveyRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        add_survey_repository_spy = AddSurveyRepositorySpy()
        sut: AddSurvey = DbAddSurvey(
          add_survey_repository=add_survey_repository_spy
        )
        return (
          sut,
          add_survey_repository_spy
        )

    def test_1_should_call_AddSurveyRepository_with_correct_email(self):
        sut, add_survey_repository_spy = self.make_sut()
        sut.add(self.params)

        assert add_survey_repository_spy.data == self.params
