from dataclasses import dataclass
from typing import Any, Optional
from shutil import Error

from ...presentation.contracts import Validation
from ...presentation.errors import MissingParamError

@dataclass
class RequiredFieldValidation(Validation):
  fieldName: str

  def validate(self, value: Any) -> Optional[Error]:
    return MissingParamError(paramName=self.fieldName)
