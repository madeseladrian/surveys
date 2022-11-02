from typing import Any, Optional
from shutil import Error

from src.presentation.contracts import Validation

class ValidationSpy(Validation):
  error: Optional[Error] = None
  value: Any

  def validate(self, value: Any) -> Optional[Error]:
    self.value = value
    return self.error
