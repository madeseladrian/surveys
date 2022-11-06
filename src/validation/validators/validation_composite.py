from dataclasses import dataclass
from typing import Any, List, Optional
from shutil import Error

from ...presentation.contracts import Validation

@dataclass
class ValidationComposite(Validation):
  validations: List[Validation]

  def validate(self, value: Any) -> Optional[Error]:
    for validation in self.validations:
      if error := validation.validate(value):
        return error
    return None
