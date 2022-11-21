from typing import List

from src.presentation.contracts import Validation
from src.validation.validators import (
  ValidationComposite,
  RequiredFieldValidation,
  EmailValidation
)
from src.utils import EmailValidatorAdapter
from src.main.usecases import make_login_validation


class TestMakeLoginValidation:
    def test_1_should_call_ValidationComposite_with_all_validations(self):
        validations: List[Validation] = [
          RequiredFieldValidation(field_name=field)
          for field in ['email', 'password']
        ]

        validations.append(
          EmailValidation(
            field_name='email',
            email_validator=EmailValidatorAdapter()
          )
        )
        validation_composite = ValidationComposite(validations)

        assert validation_composite == make_login_validation()
