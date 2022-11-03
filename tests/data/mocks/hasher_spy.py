import uuid
from src.data.contracts.cryptography import Hasher

class HasherSpy(Hasher):
  digest: str = str(uuid.uuid4())
  plaintext: str

  def hash(self, plaintext: str) -> str:
    self.plaintext = plaintext
    return self.digest
