from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Hasher(ABC):

    @abstractmethod
    def get_password_hash(self, password: str) -> str:
        raise NotImplementedError('Should implement method: get_password_hash')
