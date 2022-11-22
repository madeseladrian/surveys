from dataclasses import dataclass

# from ...domain.features import LoadAccountByToken
# from ...domain.params import LoadAccountByTokenResult
from ...data.contracts.cryptography import Decrypter
from ...data.contracts.db.account import LoadAccountByTokenRepository

@dataclass
class DbLoadAccountByToken:
    decrypter: Decrypter
    load_account_by_token_repository: LoadAccountByTokenRepository

    def load(self, access_token: str, role: str = None) -> None:
        if self.decrypter.decrypt(token=access_token):
            self.load_account_by_token_repository.load_by_token(
                token=access_token,
                role=role
            )
