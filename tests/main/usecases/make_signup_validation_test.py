from typing import List

from src.presentation.contracts import Validation
from src.validation.validators import (
    ValidationComposite,
    RequiredFieldValidation,
    CompareFieldsValidation,
    EmailValidation
)
from src.utils import EmailValidatorAdapter
from src.main.usecases import make_signup_validation


class TestMakeSignupValidation:
    def test_1_should_call_ValidationComposite_with_all_validations(self):
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
        validation_composite = ValidationComposite(validations)

        assert validation_composite == make_signup_validation()
