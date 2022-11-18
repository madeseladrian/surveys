from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Encrypter(ABC):

    @abstractmethod
    def encrypt(self, user_id: str) -> str:
        raise NotImplementedError('Should implement method: encrypt')
