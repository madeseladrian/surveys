from dataclasses import dataclass
from ...data.contracts.cryptography import Encrypter


@dataclass
class JoseAdapter(Encrypter):

    def encrypt(self, plain_password: str) -> str:
        pass
