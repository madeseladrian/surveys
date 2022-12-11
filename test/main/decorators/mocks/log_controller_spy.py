from typing import Any

from src.presentation.contracts import Controller
from src.presentation.helpers import HttpResponse, add_account


class LogControllerSpy(Controller):
    http_response: HttpResponse = add_account(True)
    request: Any = None

    def handle(self, request: Any) -> HttpResponse:
        self.request = request
        return self.http_response
