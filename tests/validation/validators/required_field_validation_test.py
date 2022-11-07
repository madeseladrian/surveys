from faker import Faker

from src.presentation.errors import MissingParamError
from src.validation.validators import RequiredFieldValidation

class TestRequiredFieldValidation:
  faker = Faker()
  fieldName: str = faker.word()

  def make_sut(self) -> RequiredFieldValidation:
    return RequiredFieldValidation(fieldName=self.fieldName)

  def test_1_should_return_a_MissingParamError_if_validation_fails(self):
    sut = self.make_sut()
    error = sut.validate({'invalidField': self.faker.word()})

    assert error == MissingParamError(paramName=self.fieldName)
