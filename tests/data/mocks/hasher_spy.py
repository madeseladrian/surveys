import uuid
from src.data.contracts.cryptography import Hasher


class HasherSpy(Hasher):
    digest: str = str(uuid.uuid4())
    plaintext: str

    def get_password_hash(self, plaintext: str) -> str:
        self.plaintext = plaintext
        return self.digest
