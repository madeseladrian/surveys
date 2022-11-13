from dataclasses import dataclass
from typing import Any

from src.presentation.contracts import Controller
from src.presentation.helpers import HttpResponse, add_account


@dataclass
class LogControllerSpy(Controller):
  http_response: HttpResponse = None
  request: Any = None

  def handle(self, request: Any) -> HttpResponse:
    self.request = request
    return add_account(True) if self.http_response is None else self.http_response
