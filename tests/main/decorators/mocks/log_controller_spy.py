from dataclasses import dataclass, field
from typing import Any

from src.presentation.contracts import Controller
from src.presentation.helpers import HttpResponse, add_account


@dataclass
class LogControllerSpy(Controller):
  http_response: HttpResponse = field(default_factory=lambda: add_account(True))
  request: Any = None

  def handle(self, request: Any) -> HttpResponse:
    self.request = request
    return self.http_response
