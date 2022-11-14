from faker import Faker
from typing import Tuple
from unittest.mock import patch

from src.domain.params import AddAccountParams
from src.domain.features import AddAccount

from src.presentation.contracts import Controller, Validation
from src.presentation.controllers import SignUpController
from src.presentation.errors import EmailInUseError, MissingParamError
from src.presentation.helpers import add_account, bad_request, forbidden, server_error

from ...domain.mocks import mock_add_account_params
from ..mocks import AddAccountSpy, ValidationSpy

class TestSignUpController:
  # SetUp
  faker = Faker()
  params: AddAccountParams = mock_add_account_params()

  SutTypes = Tuple[Controller, AddAccount, Validation]

  def make_sut(self) -> SutTypes:
    add_account_spy: AddAccount = AddAccountSpy()
    validation_spy: Validation = ValidationSpy()
    sut: Controller = SignUpController(
      add_account=add_account_spy,
      validation=validation_spy
    )

    return sut, add_account_spy, validation_spy

  def test_1_should_call_Validation_with_correct_values(self):
    sut, _, validation_spy = self.make_sut()
    request = self.params
    sut.handle(request=request)

    assert validation_spy.value == request

  def test_2_should_call_AddAccount_with_correct_values(self):
    sut, add_account_spy, _ = self.make_sut()
    request = self.params
    sut.handle(request=request)

    assert add_account_spy.params == request

  def test_3_should_return_201_if_valid_data_is_provided(self):
    sut, add_account_spy, _ = self.make_sut()
    http_response = sut.handle(request=self.params)

    assert http_response['status_code'] == 201
    assert http_response == add_account(add_account_spy.result)

  # Exceptions Tests

  def test_4_should_return_400_if_Validation_returns_an_error(self):
    sut, _, validation_spy = self.make_sut()
    validation_spy.error = MissingParamError(self.faker.word())
    http_response = sut.handle(self.params)

    assert http_response == bad_request(validation_spy.error)

  def test_5_should_return_403_if_AddAccount_returns_false(self):
    sut, add_account_spy, _ = self.make_sut()
    add_account_spy.result = False
    http_response = sut.handle(self.params)

    assert http_response == forbidden(EmailInUseError())

  @patch('tests.presentation.mocks.ValidationSpy.validate')
  def test_6_should_return_500_if_Validation_throws(self, mocker):
    sut, _, _ = self.make_sut()
    exception = Exception()
    mocker.side_effect = exception
    http_response = sut.handle(request=self.params)

    assert http_response == server_error(error=exception)

  @patch('tests.presentation.mocks.AddAccountSpy.add')
  def test_7_should_return_500_if_AddAccount_throws(self, mocker):
    sut, _, _ = self.make_sut()
    exception = Exception()
    mocker.side_effect = exception
    http_response = sut.handle(request=self.params)

    assert http_response == server_error(error=exception)
