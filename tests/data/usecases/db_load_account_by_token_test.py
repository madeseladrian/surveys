from typing import Tuple
from faker import Faker

from src.data.usecases import DbLoadAccountByToken
from ..mocks import DecrypterSpy


class TestDbLoadAccountByToken:
    # SetUp
    faker = Faker()
    token = faker.uuid4()
    role = faker.word()

    SutTypes = Tuple[
        DbLoadAccountByToken,
        DecrypterSpy
    ]

    def make_sut(self) -> SutTypes:
        decrypter_spy = DecrypterSpy()
        sut = DbLoadAccountByToken(
            decrypter=decrypter_spy
        )
        return sut, decrypter_spy

    def test_1_should_call_Decrypter_with_correct_token(self):
        sut, decrypter_spy = self.make_sut()
        sut.load(access_token=self.token, role=self.role)

        assert decrypter_spy.token == self.token

    def test_2_should_return_None_if_Decrypter_returns_None(self):
        sut, decrypter_spy = self.make_sut()
        decrypter_spy.user_id = None
        account = sut.load(access_token=self.token, role=self.role)

        assert account is None
