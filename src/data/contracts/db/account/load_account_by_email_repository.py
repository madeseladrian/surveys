from abc import ABC, abstractmethod
from ....params import LoadAccountByEmailRepositoryResult

class LoadAccountByEmailRepository(ABC):

  @abstractmethod
  def load_by_email(self, email: str) -> LoadAccountByEmailRepositoryResult:
    raise NotImplementedError('Should implement method: load_by_email')
