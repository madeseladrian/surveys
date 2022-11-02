from faker import Faker
from typing import Tuple

from src.domain.params import AddAccountParams
from src.domain.usecases import AddAccount
from src.presentation.contracts import Controller, Validation
from src.presentation.controllers import SignUpController
from src.presentation.errors import MissingParamError
from src.presentation.helpers import bad_request

from tests.presentation.mocks import AddAccountSpy, ValidationSpy

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
    request: AddAccountParams = self.params
    sut.handle(request=request)

    assert validation_spy.value == request

  def test_2_call_AddAccount_with_correct_values(self):
    sut, add_account_spy, _ = self.make_sut()
    request: AddAccountParams = self.params
    sut.handle(request=request)

    assert add_account_spy.params == request

  # Exceptions Tests

  def test_3_return_400_if_Validation_returns_an_error(self):
    sut, _, validation_spy = self.make_sut()
    validation_spy.error = MissingParamError(self.faker.word())
    httpResponse = sut.handle(self.params)

    assert httpResponse == bad_request(validation_spy.error)
