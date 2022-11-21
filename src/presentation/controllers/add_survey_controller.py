from dataclasses import dataclass
from datetime import datetime

from ...domain.features import AddSurvey
from ...domain.params import AddSurveyParams

from ..contracts import Controller, Validation
from ..helpers import (
    bad_request,
    HttpResponse,
    no_content,
    server_error
)
from ..params import AddSurveyControllerRequest


@dataclass
class AddSurveyController(Controller):
    add_survey: AddSurvey
    validation: Validation

    def handle(self, request: AddSurveyControllerRequest) -> HttpResponse:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

            self.add_survey.add(AddSurveyParams(
                question=request['question'],
                answers=request['answers'],
                date=datetime.now()
            ))
            return no_content()

        except Exception as e:
            return server_error(e)
