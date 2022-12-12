from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import LoadSurveysResult


@dataclass
class LoadSurveys(ABC):

    @abstractmethod
    def load(self, account_id: str) -> LoadSurveysResult:
        raise NotImplementedError('Should implement method: load')
