from dataclasses import dataclass
from typing import Any, Optional
from shutil import Error

from ...presentation.contracts import Validation
from ...presentation.errors import InvalidParamError

@dataclass
class CompareFieldsValidation(Validation):
  fieldName: str
  fieldToCompareName: str

  def validate(self, value: Any) -> Optional[Error]:
    return InvalidParamError(paramName=self.fieldToCompareName)
