from dataclasses import dataclass

from ..contracts import Validation
from ..params import AddSurveyControllerRequest


@dataclass
class AddSurveyController:
    validation: Validation

    def handle(self, request: AddSurveyControllerRequest) -> None:
        self.validation.validate(request)
