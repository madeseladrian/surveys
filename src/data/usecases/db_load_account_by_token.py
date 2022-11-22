from dataclasses import dataclass

# from ...domain.features import LoadAccountByToken
# from ...domain.params import LoadAccountByTokenResult
from ...data.contracts.cryptography import Decrypter


@dataclass
class DbLoadAccountByToken:
    decrypter: Decrypter

    def load(self, access_token: str, role: str = None) -> None:
        self.decrypter.decrypt(token=access_token)
