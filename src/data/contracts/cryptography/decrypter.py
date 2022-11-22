from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Decrypter(ABC):

    @abstractmethod
    def decrypt(self, token: str) -> str:
        raise NotImplementedError('Should implement method: decrypt')
