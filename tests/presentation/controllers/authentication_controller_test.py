from faker import Faker
from typing import Tuple

from src.domain.params import AuthenticationParams
from src.domain.features import Authentication

from src.presentation.contracts import Controller, Validation
from src.presentation.controllers import LoginController

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
