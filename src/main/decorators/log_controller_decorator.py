from dataclasses import dataclass
from typing import Any

from ...presentation.contracts import Controller
from ...presentation.helpers import HttpResponse


@dataclass
class LogControllerDecorator(Controller):
  controller: Controller

  def handle(self, request: Any) -> HttpResponse:
    return self.controller.handle(request)
