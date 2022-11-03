from faker import Faker
from typing import Tuple

from src.domain.params import AddAccountParams
from src.domain.usecases import AddAccount
from src.data.features import DbAddAccount

from ..mocks import CheckAccountByEmailRepositorySpy

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

  SutTypes = Tuple[AddAccount, CheckAccountByEmailRepositorySpy]

  def make_sut(self) -> SutTypes:
    check_account_by_email_repository_spy = CheckAccountByEmailRepositorySpy()
    sut: AddAccount = DbAddAccount(
      check_account_by_email_repository=check_account_by_email_repository_spy
    )
    return sut, check_account_by_email_repository_spy

  def test_1_should_call_CheckAccountByEmailRepository_with_correct_email(self):
    sut, check_account_by_email_repository_spy = self.make_sut()
    sut.add(self.params)

    assert check_account_by_email_repository_spy.email == self.params['email']
