from typing import List

from ...presentation.contracts import Validation
from ...validation.validators import (
  ValidationComposite,
  RequiredFieldValidation,
  CompareFieldsValidation,
  EmailValidation
)
from ...utils import EmailValidatorAdapter

def make_signup_validation() -> ValidationComposite:
  validations: List[Validation] = [
    RequiredFieldValidation(field_name=field)
    for field in ['name', 'email', 'password', 'password_confirmation']
  ]

  validations.extend((
    CompareFieldsValidation('password', 'password_confirmation'),
    EmailValidation(
      field_name='email',
      email_validator=EmailValidatorAdapter()
    )
  ))

  return ValidationComposite(validations=validations)
