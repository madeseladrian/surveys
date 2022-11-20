from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import AddSurveyParams


@dataclass
class AddSurvey(ABC):

    @abstractmethod
    def add(self, data: AddSurveyParams) -> None:
        raise NotImplementedError('Should implement method: add')
