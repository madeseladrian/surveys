from ...domain.features import AddAccount
from ...data.usecases import DbAddAccount

from ...infra.cryptography import BCryptAdapter
from ...infra.db.mongodb import AccountMongoRepository


def make_db_add_account() -> AddAccount:
  account_mongo_repository = AccountMongoRepository()

  return DbAddAccount(
    add_account_repository=account_mongo_repository,
    check_account_by_email_repository=account_mongo_repository,
    hasher=BCryptAdapter()
  )
