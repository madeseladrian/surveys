from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Encrypter(ABC):

  @abstractmethod
  def encrypt(self, plain_password: str) -> str:
    raise NotImplementedError('Should implement method: encrypt')
