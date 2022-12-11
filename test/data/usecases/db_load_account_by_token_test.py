from typing import Tuple
from faker import Faker
import pytest
from unittest.mock import patch

from src.data.usecases import DbLoadAccountByToken
from ..mocks import DecrypterSpy, LoadAccountByTokenRepositorySpy


class TestDbLoadAccountByToken:
    # SetUp
    faker = Faker()
    token = faker.uuid4()
    role = faker.word()

    SutTypes = Tuple[
        DbLoadAccountByToken,
        DecrypterSpy,
        LoadAccountByTokenRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        decrypter_spy = DecrypterSpy()
        load_account_by_token_repository_spy = LoadAccountByTokenRepositorySpy()
        sut = DbLoadAccountByToken(
            decrypter=decrypter_spy,
            load_account_by_token_repository=load_account_by_token_repository_spy
        )
        return sut, decrypter_spy, load_account_by_token_repository_spy

    def test_1_should_call_Decrypter_with_correct_token(self):
        sut, decrypter_spy, _ = self.make_sut()
        sut.load(access_token=self.token, role=self.role)

        assert decrypter_spy.token == self.token

    def test_2_should_return_None_if_Decrypter_returns_None(self):
        sut, decrypter_spy, _ = self.make_sut()
        decrypter_spy.user_id = None
        account = sut.load(access_token=self.token, role=self.role)

        assert account is None

    @patch('test.data.mocks.DecrypterSpy.decrypt')
    def test_3_should_throw_if_Decrypter_throws(self, mocker):
        sut, _, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.load(access_token=self.token, role=self.role)

    def test_4_should_call_LoadAccountByTokenRepository_with_correct_token(self):
        sut, _, load_account_by_token_repository_spy = self.make_sut()
        sut.load(access_token=self.token, role=self.role)

        assert load_account_by_token_repository_spy.token == self.token
        assert load_account_by_token_repository_spy.role == self.role

    def test_5_should_return_None_if_LoadAccountByTokenRepository_returns_None(self):
        sut, _, load_account_by_token_repository_spy = self.make_sut()
        load_account_by_token_repository_spy.result = None
        account = sut.load(access_token=self.token, role=self.role)

        assert account is None

    def test_6_should_return_an_account_on_success(self):
        sut, _, load_account_by_token_repository_spy = self.make_sut()
        account = sut.load(access_token=self.token, role=self.role)

        assert account == load_account_by_token_repository_spy.result

    @patch('test.data.mocks.LoadAccountByTokenRepositorySpy.load_by_token')
    def test_7_should_throw_if_LoadAccountByTokenRepository_throws(self, mocker):
        sut, _, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.load(access_token=self.token, role=self.role)
