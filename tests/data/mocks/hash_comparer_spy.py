from src.data.contracts.cryptography import HashComparer


class HashComparerSpy(HashComparer):
  plain_password: str
  hashed_password: str
  is_valid: bool = True

  def verify(self, plain_password: str, hashed_password: str) -> bool:
    self.plain_password = plain_password
    self.hashed_password = hashed_password
    return self.is_valid
