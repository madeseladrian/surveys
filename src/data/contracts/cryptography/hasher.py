from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Hasher(ABC):

  @abstractmethod
  def hash(self, plaintext: str) -> str:
    raise NotImplementedError('Should implement method: hash')
