from dataclasses import dataclass
from typing import Any, Optional
from shutil import Error

from ...presentation.contracts import Validation
from ...presentation.errors import InvalidParamError

@dataclass
class CompareFieldsValidation(Validation):
  field_name: str
  field_to_compare_name: str

  def validate(self, value: Any) -> Optional[Error]:
    if value[self.field_name] != value[self.field_to_compare_name]:
      return InvalidParamError(param_name=self.field_to_compare_name)
    return None
