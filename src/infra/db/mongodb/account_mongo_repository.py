from dataclasses import dataclass

from ....data.contracts.db.account import (
    AddAccountRepository,
    CheckAccountByEmailRepository,
    LoadAccountByEmailRepository
)
from ....data.params import (
    AddAccountRepositoryParams,
    AddAccountRepositoryResult,
    LoadAccountByEmailRepositoryResult
)
from .mongo_helper import mongohelper


@dataclass
class AccountMongoRepository(
    AddAccountRepository,
    CheckAccountByEmailRepository,
    LoadAccountByEmailRepository
):

    def add(self, data: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
        account = mongohelper.get_collection(
            collection='accounts'
        ).insert_one(dict(data))
        return account.inserted_id is not None

    def check_by_email(self, email: str) -> bool:
        account = mongohelper.get_collection(
            collection='accounts'
        ).find_one({'email': email})
        return account is not None

    def load_by_email(self, email: str) -> LoadAccountByEmailRepositoryResult:
        account = mongohelper.get_collection(
            collection='accounts'
        ).find_one({'email': email}, {
            '_id': 1, 'name': 1, 'password': 1
        })
        return mongohelper.map_collection(account) if account is not None else None
