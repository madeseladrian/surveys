from dataclasses import dataclass
from bson.objectid import ObjectId
from typing import Optional

from ....data.contracts.db.account import (
    AddAccountRepository,
    CheckAccountByEmailRepository,
    LoadAccountByEmailRepository,
    LoadAccountByTokenRepository,
    UpdateAccessTokenRepository
)
from ....data.params import (
    AddAccountRepositoryParams,
    AddAccountRepositoryResult,
    LoadAccountByEmailRepositoryResult,
    LoadAccountByTokenRepositoryResult
)
from .mongo_helper import mongohelper


@dataclass
class AccountMongoRepository(
    AddAccountRepository,
    CheckAccountByEmailRepository,
    LoadAccountByEmailRepository,
    LoadAccountByTokenRepository,
    UpdateAccessTokenRepository
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
        ).find_one({
            'email': email
        }, {
            '_id': 1,
            'name': 1,
            'password': 1
        })
        return mongohelper.map_collection(account) if account is not None else None

    def update_access_token(self, user_id: str, token: str) -> None:
        object_id = ObjectId(user_id)
        mongohelper.get_collection(
            collection='accounts'
        ).update_one({'_id': object_id}, {"$set": {'access_token': token}})

    def load_by_token(self, token: str, role: Optional[str] = None) -> Optional[LoadAccountByTokenRepositoryResult]:
        account = mongohelper.get_collection(
            collection='accounts'
        ).find_one({
            'access_token': token,
            "$or": [{
                'role': role
            }, {
                'role': 'admin'
            }]
        }, {
            '_id': 1,

        })
        return mongohelper.map_collection(account) if account is not None else None
