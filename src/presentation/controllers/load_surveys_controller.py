from dataclasses import dataclass

from ...domain.features import LoadSurveys
from ..params import LoadSurveysControllerRequest


@dataclass
class LoadSurveysController:
    load_surveys: LoadSurveys

    def handle(self, request: LoadSurveysControllerRequest) -> None:
        self.load_surveys.load(account_id=request['account_id'])
