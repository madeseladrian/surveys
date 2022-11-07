from faker import Faker
from src.presentation.errors import InvalidParamError
from src.validation.validators import CompareFieldsValidation

class TestCompareFieldsValidation:
  # SetUp
  faker = Faker()
  field_name: str = faker.word()
  field_to_compare_name: str = faker.word()

  def make_sut(self) -> CompareFieldsValidation:
    return CompareFieldsValidation(
      field_name=self.field_name,
      field_to_compare_name=self.field_to_compare_name
    )

  def test_1_should_return_an_InvalidParamError_if_validation_fails(self):
    sut = self.make_sut()
    error = sut.validate({
      self.field_name: 'any_field',
      self.field_to_compare_name: 'other_field'
    })

    assert error == InvalidParamError(self.field_to_compare_name)

  def test_2_should_return_None_if_validation_succeds(self):
    sut = self.make_sut()
    value = self.faker.word()
    error = sut.validate({
      self.field_name: value,
      self.field_to_compare_name: value
    })

    assert error is None
