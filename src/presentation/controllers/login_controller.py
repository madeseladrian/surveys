from dataclasses import dataclass

from ..contracts import Validation
from ..params import LoginControllerRequest

@dataclass
class LoginController():
  validation: Validation

  def handle(self, request: LoginControllerRequest) -> None:
    self.validation.validate(request)
