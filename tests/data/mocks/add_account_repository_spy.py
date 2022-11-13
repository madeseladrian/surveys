from data.contracts.db.account import AddAccountRepository
from src.data.params import AddAccountRepositoryParams

class AddAccountRepositorySpy(AddAccountRepository):
  params: AddAccountRepositoryParams
  result: bool = True

  def add(self, params: AddAccountRepositoryParams) -> bool:
    self.params = params
    return self.result
