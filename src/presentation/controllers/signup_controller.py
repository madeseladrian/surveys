from dataclasses import dataclass
from typing import Any

from ...domain.features import AddAccount
from ..contracts import Controller, Validation
from ..errors import EmailInUseError
from ..helpers import bad_request, forbidden, server_error
from ..params import SignUpControllerRequest
@dataclass
class SignUpController(Controller):
  add_account: AddAccount
  validation: Validation

  def handle(self, request: SignUpControllerRequest) -> Any:
    try:
      if error := self.validation.validate(request):
        return bad_request(error)

      isValid = self.add_account.add(request)
      if not isValid:
        return forbidden(EmailInUseError())

    except Exception as error:
      return server_error(error)
