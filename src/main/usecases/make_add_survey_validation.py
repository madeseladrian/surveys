from typing import List

from ...presentation.contracts import Validation
from ...validation.validators import (
    ValidationComposite,
    RequiredFieldValidation,
)


def make_add_survey_validation() -> ValidationComposite:
    validations: List[Validation] = [
        RequiredFieldValidation(field_name=field)
        for field in ['question', 'answers']
    ]

    return ValidationComposite(validations=validations)
