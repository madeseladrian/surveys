from data.contracts.db.account import AddAccountRepository
from src.data.params import AddAccountRepositoryParams, AddAccountRepositoryResult


class AddAccountRepositorySpy(AddAccountRepository):
    params: AddAccountRepositoryParams
    result: AddAccountRepositoryResult = True

    def add(self, params: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
        self.params = params
        return self.result
