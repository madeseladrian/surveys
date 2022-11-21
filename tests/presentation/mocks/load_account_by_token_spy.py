from faker import Faker

from src.domain.features import LoadAccountByToken
from src.domain.params import LoadAccountByTokenResult


faker = Faker()

class LoadAccountByTokenSpy(LoadAccountByToken):
    access_token: str
    role: str
    result: dict = {
        id: faker.uuid4()
    }

    def load(self, access_token: str, role: str = None) -> LoadAccountByTokenResult:
        self.access_token = access_token
        self.role = role
        return self.result
