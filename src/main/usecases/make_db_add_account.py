from ...domain.features import AddAccount
from ...data.usecases import DbAddAccount

from ...infra.cryptography import BCryptAdapter
from ...infra.db.mongo import AccountMongoRepository

def make_db_add_account() -> AddAccount:
  return DbAddAccount(
    add_account_repository=AccountMongoRepository(),
    check_account_by_email_repository=AccountMongoRepository(),
    hasher=BCryptAdapter()
  )
