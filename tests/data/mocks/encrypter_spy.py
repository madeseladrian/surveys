from faker import Faker
from src.data.contracts.cryptography import Encrypter


faker = Faker()

class EncrypterSpy(Encrypter):
    token: str = faker.uuid4()
    plain_password: str

    def encrypt(self, plain_password: str) -> str:
        self.plain_password = plain_password
        return self.token
