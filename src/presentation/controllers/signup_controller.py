from dataclasses import dataclass
from typing import Any

from ...domain.usecases import AddAccount
from ..contracts import Controller, Validation
from ..helpers import bad_request
from ..params import SignUpControllerRequest

@dataclass
class SignUpController(Controller):
  add_account: AddAccount
  validation: Validation

  def handle(self, request: SignUpControllerRequest) -> Any:
    if error := self.validation.validate(request):
      return bad_request(error)
    self.add_account.add(request)
