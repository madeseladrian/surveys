from faker import Faker
from typing import Tuple
from unittest.mock import patch

from src.presentation.controllers import LoadSurveysController
from src.presentation.helpers import no_content, ok, server_error
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

    def test_2_should_return_200_on_success(self):
        sut, load_surveys_spy = self.make_sut()
        http_response = sut.handle(request=self.params)

        assert http_response == ok(load_surveys_spy.result)

    def test_3_should_return_204_if_LoadSurveys_returns_empty(self):
        sut, load_surveys_spy = self.make_sut()
        load_surveys_spy.result = []
        http_response = sut.handle(request=self.params)

        assert http_response == no_content()

    @patch('test.presentation.mocks.survey.LoadSurveysSpy.load')
    def test_4_should_return_500_if_LoadSurveys_throws(self, mocker):
        sut, _ = self.make_sut()
        exception = Exception()
        mocker.side_effect = exception
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 500
        assert http_response == server_error(error=exception)
