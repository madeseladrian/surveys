from dataclasses import dataclass

from ...domain.usecases import AddAccount
from ...domain.params import AddAccountParams
from ..contracts.cryptography import Hasher
from ..contracts.db import CheckAccountByEmailRepository

@dataclass
class DbAddAccount(AddAccount):
  check_account_by_email_repository: CheckAccountByEmailRepository
  hasher: Hasher

  def add(self, account: AddAccountParams) -> bool:
    exists = self.check_account_by_email_repository.check_by_email(email=account['email'])
    isValid = False

    if not exists:
      self.hasher.hash(account['password'])
      isValid = True
    return isValid
