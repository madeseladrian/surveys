from typing import List

from ...presentation.contracts import Validation
from ...validation.validators import (
  ValidationComposite,
  RequiredFieldValidation,
  EmailValidation
)
from ...utils import EmailValidatorAdapter


def make_login_validation() -> ValidationComposite:
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

    return ValidationComposite(validations=validations)
