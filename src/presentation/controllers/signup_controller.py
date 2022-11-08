from dataclasses import dataclass

from ...domain.features import AddAccount
from ...domain.params import AddAccountParams

from ..contracts import Controller, Validation
from ..errors import EmailInUseError
from ..helpers import (
  add_account,
  bad_request,
  forbidden,
  HttpResponse,
  server_error
)
from ..params import SignUpControllerRequest

@dataclass
class SignUpController(Controller):
  add_account: AddAccount
  validation: Validation

  def handle(self, request: SignUpControllerRequest) -> HttpResponse:
    try:
      if error := self.validation.validate(request):
        return bad_request(error)

      if is_valid := self.add_account.add(AddAccountParams(
        name=request['name'],
        email=request['email'],
        password=request['password']
      )):
        return add_account(data=is_valid)
      return forbidden(EmailInUseError())

    except Exception as error:
      return server_error(error)
