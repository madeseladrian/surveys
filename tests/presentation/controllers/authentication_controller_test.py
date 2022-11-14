from faker import Faker
from typing import Tuple

from src.domain.params import AuthenticationParams

from src.presentation.contracts import Controller, Validation
from src.presentation.controllers import LoginController

from ...domain.mocks import mock_authentication_params
from ..mocks import ValidationSpy

class TestAuthenticationController:
  # SetUp
  faker = Faker()
  params: AuthenticationParams = mock_authentication_params()

  SutTypes = Tuple[Controller, Validation]

  def make_sut(self) -> SutTypes:
    validation_spy: Validation = ValidationSpy()
    sut: Controller = LoginController(
      validation=validation_spy
    )

    return sut, validation_spy

  def test_1_should_call_Validation_with_correct_values(self):
    sut, validation_spy = self.make_sut()
    request = self.params
    sut.handle(request=request)

    assert validation_spy.value == request
