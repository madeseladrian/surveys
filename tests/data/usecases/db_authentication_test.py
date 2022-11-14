from typing import Tuple

from src.domain.params import AuthenticationParams
from src.domain.features import Authentication
from src.data.usecases import DbAuthentication

from ...domain.mocks import mock_authentication_params
from ..mocks import LoadAccountByEmailRepositorySpy


class TestDbAuthentication:
  # SetUp
  params: AuthenticationParams = mock_authentication_params()

  SutTypes = Tuple[
    Authentication,
    LoadAccountByEmailRepositorySpy
  ]

  def make_sut(self) -> SutTypes:
    load_account_by_email_repository_spy = LoadAccountByEmailRepositorySpy()
    sut: DbAuthentication = DbAuthentication(
      loadAccount_by_email_repository=load_account_by_email_repository_spy
    )
    return (
      sut,
      load_account_by_email_repository_spy
    )

  # Success Tests

  def test_1_should_call_LoadAccountByEmailRepository_with_correct_email(self):
    sut, load_account_by_email_repository_spy = self.make_sut()
    sut.auth(self.params)

    assert load_account_by_email_repository_spy.email == self.params['email']
