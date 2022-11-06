from faker import Faker
from typing import List, Tuple
from shutil import Error

from src.presentation.contracts.validation import Validation
from src.presentation.errors import MissingParamError
from src.validation.validators import ValidationComposite

from ...presentation.mocks import ValidationSpy

class TestValidationComposite:
  faker = Faker()
  field: str = faker.word()

  SutTypes = Tuple[ValidationComposite, List[Validation]]

  def make_sut(self) -> SutTypes:
    validation_spies: List[Validation] = [
      ValidationSpy(),
      ValidationSpy()
    ]
    sut = ValidationComposite(validation_spies)
    return sut, validation_spies

  def test_1_should_return_an_error_if_any_validation_fails(self):
    sut, validation_spies = self.make_sut()
    validation_spies[1].error = MissingParamError(self.field)
    error = sut.validate({self.field: self.faker.word()})

    assert error == validation_spies[1].error

  def test_2_should_return_the_first_error_if_more_then_one_validation_fails(self):
    sut, validation_spies = self.make_sut()
    validation_spies[0].error = Error
    validation_spies[1].error = MissingParamError(self.field)
    error = sut.validate({self.field: self.faker.word()})

    assert error == validation_spies[0].error
