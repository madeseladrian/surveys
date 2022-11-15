from dataclasses import dataclass
from typing import Any, Optional

from ...presentation.contracts import Validation
from ...presentation.errors import InvalidParamError
from ..contracts import EmailValidator


@dataclass
class EmailValidation(Validation):
    field_name: str
    email_validator: EmailValidator

    def validate(self, value: Any) -> Optional[Exception]:
        is_valid = self.email_validator.is_valid(value[self.field_name])
        return None if is_valid else InvalidParamError(self.field_name)
