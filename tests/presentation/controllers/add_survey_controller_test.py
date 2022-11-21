from datetime import datetime
from faker import Faker
from typing import Tuple
from unittest.mock import patch

from src.domain.features import AddSurvey
from src.domain.params import AddSurveyParams

from src.presentation.contracts import Controller, Validation
from src.presentation.controllers import AddSurveyController
from src.presentation.errors import MissingParamError
from src.presentation.helpers import bad_request, server_error

from ...domain.mocks import mock_add_survey_params
from ..mocks import AddSurveySpy, ValidationSpy


class TestAddSurveyController:
    # SetUp
    faker = Faker()
    params: AddSurveyParams = mock_add_survey_params()

    SutTypes = Tuple[
        Controller,
        AddSurveySpy,
        ValidationSpy
    ]

    def make_sut(self) -> SutTypes:
        add_survey_spy: AddSurvey = AddSurveySpy()
        validation_spy: Validation = ValidationSpy()
        sut = AddSurveyController(
            add_survey=add_survey_spy,
            validation=validation_spy
        )

        return sut, add_survey_spy, validation_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, _, validation_spy = self.make_sut()
        request = self.params
        sut.handle(request=request)

        assert validation_spy.value == request

    def test_2_should_return_400_if_Validation_returns_an_error(self):
        sut, _, validation_spy = self.make_sut()
        validation_spy.error = MissingParamError(self.faker.word())
        http_response = sut.handle(self.params)

        assert http_response['status_code'] == 400
        assert http_response == bad_request(validation_spy.error)

    @patch('tests.presentation.mocks.ValidationSpy.validate')
    def test_3_should_return_500_if_Validation_throws(self, mocker):
        sut, _, _ = self.make_sut()
        exception = Exception()
        mocker.side_effect = exception
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 500
        assert http_response == server_error(error=exception)

    def test_4_should_call_AddSurvey_with_correct_values(self):
        sut, add_survey_spy, _ = self.make_sut()
        request = {**self.params, 'date': datetime.now()}
        sut.handle(request=request)

        assert add_survey_spy.params == request

    def test_5_should_return_204_if_valid_data_is_provided(self):
        sut, _, _ = self.make_sut()
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 204
        assert http_response['body'] is None

    def test_6_should_return_204_if_valid_data_is_not_provided(self):
        sut, add_survey_spy, _ = self.make_sut()
        http_response = sut.handle(request=self.params)

        assert http_response['body'] is None

    @patch('tests.presentation.mocks.AddSurveySpy.add')
    def test_7_should_return_500_if_AddSurvey_throws(self, mocker):
        sut, _, _ = self.make_sut()
        exception = Exception()
        mocker.side_effect = exception
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 500
        assert http_response == server_error(error=exception)
