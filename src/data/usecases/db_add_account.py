from dataclasses import dataclass

from ...domain.features import AddAccount
from ...domain.params import AddAccountParams, AddAccountResult
from ..contracts.cryptography import Hasher
from ..contracts.db.account import AddAccountRepository, CheckAccountByEmailRepository


@dataclass
class DbAddAccount(AddAccount):
    add_account_repository: AddAccountRepository
    check_account_by_email_repository: CheckAccountByEmailRepository
    hasher: Hasher

    def add(self, account: AddAccountParams) -> AddAccountResult:
        exists = self.check_account_by_email_repository.check_by_email(email=account['email'])
        is_valid = False

        if not exists:
            hashed_password = self.hasher.hash(account['password'])
            data = account.copy()
            data.update({'password': hashed_password})

            is_valid = self.add_account_repository.add(data)
        return is_valid
