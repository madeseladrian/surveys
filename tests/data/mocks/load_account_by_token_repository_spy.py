from faker import Faker
from typing import Optional

from src.data.contracts.db.account import LoadAccountByTokenRepository
from src.data.params import LoadAccountByTokenRepositoryResult


faker = Faker()

class LoadAccountByTokenRepositorySpy(LoadAccountByTokenRepository):
    token: str
    role: Optional[str]
    result: Optional[LoadAccountByTokenRepositoryResult] = LoadAccountByTokenRepositoryResult(id=faker.uuid4())

    def load_by_token(self, token: str, role: Optional[str] = None) -> Optional[LoadAccountByTokenRepositoryResult]:
        self.token = token
        self.role = role
        return self.result
