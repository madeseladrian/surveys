from dataclasses import dataclass

from ...domain.usecases import AddAccount
from ...domain.params import AddAccountParams
from ..contracts.db import CheckAccountByEmailRepository

@dataclass
class DbAddAccount(AddAccount):
  check_account_by_email_repository: CheckAccountByEmailRepository

  def add(self, account: AddAccountParams) -> bool:
    self.check_account_by_email_repository.check_by_email(email=account['email'])
    return True
