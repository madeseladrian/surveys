from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class EmailValidator(ABC):

  @abstractmethod
  def is_valid(self, email: str) -> bool:
    raise NotImplementedError('Should implement method: is_valid')
