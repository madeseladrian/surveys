from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from src.domain.params import LoadAccountByTokenResult


@dataclass
class LoadAccountByToken(ABC):

    @abstractmethod
    def load(self, access_token: str, role: Optional[str] = None) -> Optional[LoadAccountByTokenResult]:
        raise NotImplementedError('Should implement method: load')
