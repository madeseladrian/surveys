from abc import ABC, abstractmethod
from ...params import AddAccountRepositoryParams

class AddAccountRepository(ABC):

  @abstractmethod
  def add(self, data: AddAccountRepositoryParams) -> bool:
    raise NotImplementedError('Should implement method: add')
