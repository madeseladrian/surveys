from abc import ABC, abstractmethod
from ....params import AddSurveyRepositoryParams


class AddSurveyRepository(ABC):

    @abstractmethod
    def add(self, data: AddSurveyRepositoryParams) -> None:
        raise NotImplementedError('Should implement method: add')
