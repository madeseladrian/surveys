from ...domain.features import LoadAccountByToken
from ...data.usecases import DbLoadAccountByToken

from ...infra.cryptography import JoseAdapter
from ...infra.db.mongodb import AccountMongoRepository

from ..config.database import settings


def make_db_load_account_by_token() -> LoadAccountByToken:
    jose_adapter = JoseAdapter(
        algorithm=settings.algorithm,
        expire_in_days=settings.access_token_expire_days,
        key=settings.secret_key
    )
    account_mongo_repository = AccountMongoRepository()

    return DbLoadAccountByToken(
        decrypter=jose_adapter,
        load_account_by_token_repository=account_mongo_repository
    )
