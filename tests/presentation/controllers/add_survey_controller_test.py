from faker import Faker
from typing import Tuple

from src.domain.params import AddSurveyParams

from src.presentation.contracts import Validation
from src.presentation.controllers import AddSurveyController
from src.presentation.errors import MissingParamError
from src.presentation.helpers import bad_request

from ...domain.mocks import mock_add_survey_params
from ..mocks import ValidationSpy

class TestAddSurveyController:
    # SetUp
    faker = Faker()
    params: AddSurveyParams = mock_add_survey_params()

    SutTypes = Tuple[
        AddSurveyController,
        ValidationSpy
    ]

    def make_sut(self) -> SutTypes:
        validation_spy: Validation = ValidationSpy()
        sut = AddSurveyController(
          validation=validation_spy
        )

        return sut, validation_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, validation_spy = self.make_sut()
        request = self.params
        sut.handle(request=request)

        assert validation_spy.value == request

    def test_2_should_return_400_if_Validation_returns_an_error(self):
        sut, validation_spy = self.make_sut()
        validation_spy.error = MissingParamError(self.faker.word())
        http_response = sut.handle(self.params)

        assert http_response['status_code'] == 400
        assert http_response == bad_request(validation_spy.error)
