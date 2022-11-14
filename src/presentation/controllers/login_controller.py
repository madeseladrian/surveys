from dataclasses import dataclass

from ...domain.features import Authentication
from ..contracts import Validation
from ..params import LoginControllerRequest

@dataclass
class LoginController():
  authentication: Authentication
  validation: Validation

  def handle(self, request: LoginControllerRequest) -> None:
    self.validation.validate(request)
    self.authentication.auth(request)
