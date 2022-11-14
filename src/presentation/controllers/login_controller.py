from dataclasses import dataclass

from ...domain.features import Authentication
from ..contracts import Controller, Validation
from ..helpers import ok, HttpResponse
from ..params import LoginControllerRequest

@dataclass
class LoginController(Controller):
  authentication: Authentication
  validation: Validation

  def handle(self, request: LoginControllerRequest) -> HttpResponse:
    self.validation.validate(request)
    authentication_model = self.authentication.auth(request)
    return ok(authentication_model)
