from faker import Faker
from typing import Tuple

from src.domain.params import AddAccountParams
from src.presentation.contracts import Controller, Validation
from src.presentation.controllers import SignUpController

from tests.presentation.mocks import ValidationSpy

class TestSignUpController:
  # SetUp
  faker = Faker()
  name: str = faker.name()
  email: str = faker.email()
  password: str = faker.password()
  params: AddAccountParams = AddAccountParams(
    name=name,
    email=email,
    password=password
  )

  SutTypes = Tuple[Controller, Validation]

  def make_sut(self) -> SutTypes:
    validation_spy: Validation = ValidationSpy()
    sut: Controller = SignUpController(
      validation=validation_spy
    )

    return sut, validation_spy

  def test_1_should_call_Validation_with_correct_values(self):
    sut, validation_spy = self.make_sut()
    request: AddAccountParams = self.params
    sut.handle(request=request)

    assert validation_spy.value == request
