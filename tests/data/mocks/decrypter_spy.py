from faker import Faker
from src.data.contracts.cryptography import Decrypter


faker = Faker()

class DecrypterSpy(Decrypter):
    user_id: str = faker.uuid4()
    token: str

    def decrypt(self, token: str) -> str:
        self.token = token
        return self.user_id
