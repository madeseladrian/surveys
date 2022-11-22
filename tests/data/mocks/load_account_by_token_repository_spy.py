from faker import Faker

from src.data.contracts.db.account import LoadAccountByTokenRepository
from src.data.params import LoadAccountByTokenRepositoryResult


faker = Faker()

class LoadAccountByTokenRepositorySpy(LoadAccountByTokenRepository):
    token: str
    role: str
    result: dict = {
        'id': faker.uuid4()
    }

    def load_by_token(self, token: str, role: str = None) -> LoadAccountByTokenRepositoryResult:
        self.token = token
        self.role = role
        return self.result
