from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class HashComparer(ABC):

  @abstractmethod
  def verify(self, plain_password: str, hashed_password: str) -> str:
    raise NotImplementedError('Should implement method: verify')
