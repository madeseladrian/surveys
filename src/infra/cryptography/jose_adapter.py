from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from jose import jwt

from ...data.contracts.cryptography import Encrypter, Decrypter


@dataclass
class JoseAdapter(Encrypter, Decrypter):
    algorithm: str
    expire_in_days: int
    key: str

    def encrypt(self, user_id: str) -> str:
        expire = datetime.now(timezone.utc) + timedelta(days=self.expire_in_days)
        to_encode = {'user_id': user_id, 'exp': expire}

        return jwt.encode(
            claims=to_encode,
            key=self.key,
            algorithm=self.algorithm
        )

    def decrypt(self, token: str) -> str:
        payload = jwt.decode(
            token=token,
            key=self.key,
            algorithms=[self.algorithm]
        )
        return payload.get('user_id')
