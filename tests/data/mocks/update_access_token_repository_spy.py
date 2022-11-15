from src.data.contracts.db.account import UpdateAccessTokenRepository


class UpdateAccessTokenRepositorySpy(UpdateAccessTokenRepository):
  id: str
  token: str

  def update_access_token(self, id: str, token: str) -> None:
    self.id = id
    self.token = token
