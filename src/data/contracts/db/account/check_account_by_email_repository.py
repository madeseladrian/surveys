from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CheckAccountByEmailRepository(ABC):

    @abstractmethod
    def check_by_email(self, email: str) -> bool:
        raise NotImplementedError('Should implement method: check_by_email')
