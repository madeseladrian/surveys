from abc import ABC, abstractmethod
from dataclasses import dataclass
from faker import Faker
from typing import Any, Optional, Tuple, TypedDict
from shutil import Error

from src.domain.params import AddAccountParams

class HttpResponse(TypedDict):
  status_code: int
  body: Any

class Controller(ABC):
  @abstractmethod
  def handle(self, request: Any) -> HttpResponse:
    raise NotImplementedError('Should implement method: handle')

class Validation(ABC):
  @abstractmethod
  def validate(self, value: Any) -> Optional[Error]:
    raise NotImplementedError('Should implement method: validate')

class ValidationSpy(Validation):
  error: Optional[Error] = None
  value: Any

  def validate(self, value: Any) -> Optional[Error]:
    self.value = value
    return self.error

class SignUpControllerRequest(TypedDict):
  name: str
  email: str
  password: str

@dataclass
class SignUpController(Controller):
  validation: Validation

  def handle(self, request: SignUpControllerRequest) -> Any:
    self.validation.validate(request)

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

  def test_1_should_call_Validation_with_correct_value(self):
    sut, validation_spy = self.make_sut()
    request: AddAccountParams = self.params
    sut.handle(request=request)

    assert validation_spy.value == request
