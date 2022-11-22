from abc import ABC, abstractmethod
from typing import Optional

from ....params import LoadAccountByTokenRepositoryResult


class LoadAccountByTokenRepository(ABC):

    @abstractmethod
    def load_by_token(self, token: str, role: str = None) -> Optional[LoadAccountByTokenRepositoryResult]:
        raise NotImplementedError('Should implement method: load_by_token')
