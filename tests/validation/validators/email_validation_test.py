from faker import Faker
from typing import Tuple

from src.validation.validators import EmailValidation
from ..mocks import EmailValidatorSpy

class TestEmailValidation:
  # SetUp
  faker = Faker()
  field_name: str = faker.word()

  SutTypes = Tuple[EmailValidation, EmailValidatorSpy]

  def make_sut(self) -> SutTypes:
    email_validation_spy = EmailValidatorSpy()
    sut = EmailValidation(
      field_name=self.field_name,
      email_validator=email_validation_spy
    )
    return sut, email_validation_spy

  def test_1_should_call_EmailValidator_with_correct_email(self):
    sut, email_validator_spy = self.make_sut()
    email = self.faker.email()
    sut.validate({self.field_name: email})

    assert email_validator_spy.email == email
