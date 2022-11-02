from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import AddAccountParams

@dataclass
class AddAccount(ABC):

  @abstractmethod
  def add(self, account: AddAccountParams) -> bool:
    raise NotImplementedError('Should implement method: add')
