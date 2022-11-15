from data.contracts.db.account import CheckAccountByEmailRepository


class CheckAccountByEmailRepositorySpy(CheckAccountByEmailRepository):
  email: str
  result: bool = False

  def check_by_email(self, email: str) -> bool:
    self.email = email
    return self.result
