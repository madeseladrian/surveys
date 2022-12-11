from src.data.params import AddSurveyRepositoryParams
from src.data.contracts.db.survey import AddSurveyRepository


class AddSurveyRepositorySpy(AddSurveyRepository):
    data: AddSurveyRepositoryParams

    def add(self, data: AddSurveyRepositoryParams) -> None:
        self.data = data
