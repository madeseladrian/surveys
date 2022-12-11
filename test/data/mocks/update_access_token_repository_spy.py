from src.data.contracts.db.account import UpdateAccessTokenRepository


class UpdateAccessTokenRepositorySpy(UpdateAccessTokenRepository):
    user_id: str
    token: str

    def update_access_token(self, user_id: str, token: str) -> None:
        self.user_id = user_id
        self.token = token
