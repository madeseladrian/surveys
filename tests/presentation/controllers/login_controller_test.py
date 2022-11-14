from faker import Faker
from typing import Tuple
from unittest.mock import patch

from src.domain.params import AuthenticationParams
from src.domain.features import Authentication

from src.presentation.contracts import Controller, Validation
from src.presentation.controllers import LoginController
from src.presentation.helpers import (
  bad_request,
  ok,
  server_error,
  unauthorized
)
from src.presentation.errors import MissingParamError

from ...domain.mocks import mock_authentication_params
from ..mocks import AuthenticationSpy, ValidationSpy

class TestAuthenticationController:
  # SetUp
  faker = Faker()
  params: AuthenticationParams = mock_authentication_params()

  SutTypes = Tuple[Controller, Authentication, Validation]

  def make_sut(self) -> SutTypes:
    authentication_spy: Authentication = AuthenticationSpy()
    validation_spy: Validation = ValidationSpy()
    sut: Controller = LoginController(
      authentication=authentication_spy,
      validation=validation_spy
    )

    return sut, authentication_spy, validation_spy

  def test_1_should_call_Validation_with_correct_values(self):
    sut, _, validation_spy = self.make_sut()
    request = self.params
    sut.handle(request=request)

    assert validation_spy.value == request

  def test_2_should_call_Authentication_with_correct_values(self):
    sut, authentication_spy, _ = self.make_sut()
    request = self.params
    sut.handle(request=request)

    assert authentication_spy.params == request

  def test_3_should_return_200_if_valid_data_is_provided(self):
    sut, authentication_spy, _ = self.make_sut()
    http_response = sut.handle(request=self.params)

    assert http_response['status_code'] == 200
    assert http_response == ok(authentication_spy.result)

  # Exceptions Tests

  def test_4_should_return_400_if_Validation_returns_an_error(self):
    sut, _, validation_spy = self.make_sut()
    validation_spy.error = MissingParamError(self.faker.word())
    http_response = sut.handle(self.params)

    assert http_response['status_code'] == 400
    assert http_response == bad_request(validation_spy.error)

  def test_5_should_return_401_if_invalid_credentials_are_provided(self):
    sut, add_account_spy, _ = self.make_sut()
    add_account_spy.result = None
    http_response = sut.handle(self.params)

    assert http_response['status_code'] == 401
    assert http_response == unauthorized()

  @patch('tests.presentation.mocks.ValidationSpy.validate')
  def test_6_should_return_500_if_Validation_throws(self, mocker):
    sut, _, _ = self.make_sut()
    exception = Exception()
    mocker.side_effect = exception
    http_response = sut.handle(request=self.params)

    assert http_response['status_code'] == 500
    assert http_response == server_error(error=exception)

  @patch('tests.presentation.mocks.AuthenticationSpy.auth')
  def test_7_should_return_500_if_AddAccount_throws(self, mocker):
    sut, _, _ = self.make_sut()
    exception = Exception()
    mocker.side_effect = exception
    http_response = sut.handle(request=self.params)

    assert http_response['status_code'] == 500
    assert http_response == server_error(error=exception)
