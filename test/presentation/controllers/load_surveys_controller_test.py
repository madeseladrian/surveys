from faker import Faker
from typing import Tuple

from src.presentation.controllers import LoadSurveysController
from src.presentation.params import LoadSurveysControllerRequest

from ..mocks.survey import LoadSurveysSpy


faker = Faker()

class TestAddSurveyController:
    # SetUp
    faker = Faker()
    params = LoadSurveysControllerRequest(account_id=faker.uuid4())

    SutTypes = Tuple[
        LoadSurveysController,
        LoadSurveysSpy
    ]

    def make_sut(self) -> SutTypes:
        load_surveys_spy = LoadSurveysSpy()
        sut = LoadSurveysController(
            load_surveys=load_surveys_spy
        )

        return sut, load_surveys_spy

    def test_1_should_call_LoadSurveys_with_correct_value(self):
        sut, load_surveys_spy = self.make_sut()
        sut.handle(request=self.params)

        assert load_surveys_spy.account_id == self.params['account_id']
