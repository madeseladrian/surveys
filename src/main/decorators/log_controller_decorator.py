from dataclasses import dataclass
from typing import Any

from ...presentation.contracts import Controller
from ...presentation.helpers import HttpResponse
from ...data.contracts.db.log import LogErrorRepository


@dataclass
class LogControllerDecorator(Controller):
  controller: Controller
  log_error_repository: LogErrorRepository

  def handle(self, request: Any) -> HttpResponse:
    http_response = self.controller.handle(request)
    if http_response['status_code'] == 500:
      self.log_error_repository.log_error(http_response['body'].stack)
    return http_response
