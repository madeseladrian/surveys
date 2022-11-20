from dataclasses import dataclass

from ..contracts import Controller, Validation
from ..helpers import bad_request, HttpResponse, server_error
from ..params import AddSurveyControllerRequest

@dataclass
class AddSurveyController(Controller):
    validation: Validation

    def handle(self, request: AddSurveyControllerRequest) -> HttpResponse:
        try:
            error = self.validation.validate(request)
            return bad_request(error)

        except Exception as e:
            return server_error(e)
