from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import AddAccountParams, AddAccountResult

@dataclass
class AddAccount(ABC):

  @abstractmethod
  def add(self, account: AddAccountParams) -> AddAccountResult:
    raise NotImplementedError('Should implement method: add')
