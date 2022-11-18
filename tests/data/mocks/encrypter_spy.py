from faker import Faker
from src.data.contracts.cryptography import Encrypter


faker = Faker()

class EncrypterSpy(Encrypter):
    token: str = faker.uuid4()
    user_id: str

    def encrypt(self, user_id: str) -> str:
        self.user_id = user_id
        return self.token
