from dataclasses import dataclass

from ...domain.params import AuthenticationParams
from ..contracts.cryptography import Encrypter, HashComparer
from ..contracts.db.account import (
  LoadAccountByEmailRepository,
  UpdateAccessTokenRepository
)

@dataclass
class DbAuthentication:

  encrypter: Encrypter
  hash_comparer: HashComparer
  loadAccount_by_email_repository: LoadAccountByEmailRepository
  update_access_token_repository: UpdateAccessTokenRepository

  def auth(self, authentication: AuthenticationParams) -> None:
    if account := self.loadAccount_by_email_repository.load_by_email(
      email=authentication['email']
    ):
      if self.hash_comparer.verify(
        plain_password=authentication['password'],
        hashed_password=account['password']
      ):
        access_token = self.encrypter.encrypt(plain_password=account['id'])
        self.update_access_token_repository.update_access_token(
          id=account['id'],
          token=access_token
        )
