from abc import ABC, abstractmethod
from ....params import LoadAccountByTokenRepositoryResult


class LoadAccountByTokenRepository(ABC):

    @abstractmethod
    def load_by_token(self, token: str, role: str = None) -> LoadAccountByTokenRepositoryResult:
        raise NotImplementedError('Should implement method: load_by_token')
