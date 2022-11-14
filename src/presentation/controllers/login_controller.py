from dataclasses import dataclass

from ...domain.features import Authentication
from ..contracts import Controller, Validation
from ..helpers import bad_request, HttpResponse, ok
from ..params import LoginControllerRequest

@dataclass
class LoginController(Controller):
  authentication: Authentication
  validation: Validation

  def handle(self, request: LoginControllerRequest) -> HttpResponse:
    if error := self.validation.validate(request):
      return bad_request(error)
    authentication_model = self.authentication.auth(request)
    return ok(authentication_model)
