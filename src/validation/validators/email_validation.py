from dataclasses import dataclass
from typing import Any

from ...presentation.contracts import Validation
from ..contracts import EmailValidator

@dataclass
class EmailValidation(Validation):
  field_name: str
  email_validator: EmailValidator

  def validate(self, value: Any) -> Any:
    self.email_validator.is_valid(value[self.field_name])
