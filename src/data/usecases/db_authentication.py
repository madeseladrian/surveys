from dataclasses import dataclass

from ...domain.params import AuthenticationParams
from ..contracts.db.account import LoadAccountByEmailRepository

@dataclass
class DbAuthentication():
  loadAccount_by_email_repository: LoadAccountByEmailRepository

  def auth(self, authentication: AuthenticationParams) -> None:
    self.loadAccount_by_email_repository.load_by_email(authentication['email'])
