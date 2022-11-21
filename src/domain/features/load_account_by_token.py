from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import LoadAccountByTokenResult


@dataclass
class LoadAccountByToken(ABC):

    @abstractmethod
    def load(self, access_token: str, role: str = None) -> LoadAccountByTokenResult:
        raise NotImplementedError('Should implement method: load')
