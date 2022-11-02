from dataclasses import dataclass
from typing import Any

from ...domain.usecases import AddAccount
from ..contracts import Controller, Validation
from ..params import SignUpControllerRequest

@dataclass
class SignUpController(Controller):
  add_account: AddAccount
  validation: Validation

  def handle(self, request: SignUpControllerRequest) -> Any:
    self.add_account.add(request)
    self.validation.validate(request)
