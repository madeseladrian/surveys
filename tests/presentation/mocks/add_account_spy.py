from src.domain.usecases import AddAccount
from src.domain.params import AddAccountParams

class AddAccountSpy(AddAccount):
  params: AddAccountParams
  result: bool = True

  def add(self, params: AddAccountParams) -> bool:
    self.params = params
    return self.result
