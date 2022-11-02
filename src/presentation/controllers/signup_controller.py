from dataclasses import dataclass
from typing import Any

from ..contracts import Controller, Validation
from ..params import SignUpControllerRequest

@dataclass
class SignUpController(Controller):
  validation: Validation

  def handle(self, request: SignUpControllerRequest) -> Any:
    self.validation.validate(request)
