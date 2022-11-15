from dataclasses import dataclass
from passlib.context import CryptContext

from ...data.contracts.cryptography import HashComparer, Hasher


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@dataclass
class BCryptAdapter(Hasher, HashComparer):

    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
