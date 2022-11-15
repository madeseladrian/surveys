from dataclasses import dataclass

from ...domain.features import Authentication
from ..contracts import Controller, Validation
from ..helpers import (
  bad_request,
  HttpResponse,
  ok,
  server_error,
  unauthorized
)
from ..params import LoginControllerRequest


@dataclass
class LoginController(Controller):
    authentication: Authentication
    validation: Validation

    def handle(self, request: LoginControllerRequest) -> HttpResponse:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)
            authentication_model = self.authentication.auth(request)
            return ok(authentication_model) if authentication_model else unauthorized()

        except Exception as e:
            return server_error(e)
