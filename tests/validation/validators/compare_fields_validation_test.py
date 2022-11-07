from faker import Faker
from src.presentation.errors import InvalidParamError
from src.validation.validators import CompareFieldsValidation

class TestCompareFieldsValidation:
  # SetUp
  faker = Faker()
  fieldName: str = faker.word()
  fieldToCompareName: str = faker.word()

  def make_sut(self) -> CompareFieldsValidation:
    return CompareFieldsValidation(
      fieldName=self.fieldName,
      fieldToCompareName=self.fieldToCompareName
    )

  def test_1_should_return_an_InvalidParamError_if_validation_fails(self):
    sut = self.make_sut()
    error = sut.validate({
      self.fieldName: 'any_field',
      self.fieldToCompareName: 'other_field'
    })

    assert error == InvalidParamError(self.fieldToCompareName)
