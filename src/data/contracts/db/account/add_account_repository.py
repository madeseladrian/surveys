from abc import ABC, abstractmethod
from ....params import AddAccountRepositoryParams, AddAccountRepositoryResult

class AddAccountRepository(ABC):

    @abstractmethod
    def add(self, data: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
        raise NotImplementedError('Should implement method: add')
