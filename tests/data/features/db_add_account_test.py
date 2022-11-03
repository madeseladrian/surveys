from faker import Faker
from typing import Tuple

from src.domain.params import AddAccountParams
from src.domain.usecases import AddAccount
from src.data.features import DbAddAccount

from ..mocks import CheckAccountByEmailRepositorySpy, HasherSpy

class TestDbAddAccount:
  # SetUp
  faker = Faker()
  name: str = faker.name()
  email: str = faker.email()
  password: str = faker.password()
  params: AddAccountParams = AddAccountParams(
    name=name,
    email=email,
    password=password
  )

  SutTypes = Tuple[
    AddAccount,
    CheckAccountByEmailRepositorySpy,
    HasherSpy
  ]

  def make_sut(self) -> SutTypes:
    check_account_by_email_repository_spy = CheckAccountByEmailRepositorySpy()
    hasher_spy = HasherSpy()
    sut: AddAccount = DbAddAccount(
      check_account_by_email_repository=check_account_by_email_repository_spy,
      hasher=hasher_spy
    )
    return sut, check_account_by_email_repository_spy, hasher_spy

  def test_1_should_call_CheckAccountByEmailRepository_with_correct_email(self):
    sut, check_account_by_email_repository_spy, _ = self.make_sut()
    sut.add(self.params)

    assert check_account_by_email_repository_spy.email == self.params['email']

  def test_2_should_return_true_if_CheckAccountByEmailRepository_returns_false(self):
    sut, _, _ = self.make_sut()
    is_valid = sut.add(self.params)

    assert is_valid

  def test_3_should_call_Hasher_with_correct_plaintext(self):
    sut, _, hasher_spy = self.make_sut()
    sut.add(self.params)

    assert hasher_spy.plaintext == self.params['password']
