import pytest
from typing import Tuple
from unittest.mock import patch

from src.domain.params import AuthenticationParams
from src.domain.features import Authentication
from src.data.usecases import DbAuthentication

from ...domain.mocks import mock_authentication_params
from ..mocks import HashComparerSpy, LoadAccountByEmailRepositorySpy


class TestDbAuthentication:
  # SetUp
  params: AuthenticationParams = mock_authentication_params()

  SutTypes = Tuple[
    Authentication,
    HashComparerSpy,
    LoadAccountByEmailRepositorySpy
  ]

  def make_sut(self) -> SutTypes:
    hash_comparer_spy = HashComparerSpy()
    load_account_by_email_repository_spy = LoadAccountByEmailRepositorySpy()
    sut: DbAuthentication = DbAuthentication(
      hash_comparer=hash_comparer_spy,
      loadAccount_by_email_repository=load_account_by_email_repository_spy
    )
    return (
      sut,
      hash_comparer_spy,
      load_account_by_email_repository_spy
    )

  def test_1_should_call_LoadAccountByEmailRepository_with_correct_email(self):
    sut, _, load_account_by_email_repository_spy = self.make_sut()
    sut.auth(self.params)

    assert load_account_by_email_repository_spy.email == self.params['email']

  def test_2_should_return_None_if_LoadAccountByEmailRepository_returns_None(self):
    sut, _, load_account_by_email_repository_spy = self.make_sut()
    load_account_by_email_repository_spy.result = None
    authentication_model = sut.auth(self.params)

    assert authentication_model is None

  @patch('tests.data.mocks.LoadAccountByEmailRepositorySpy.load_by_email')
  def test_3_should_return_an_error_if_LoadAccountByEmailRepository_throws(self, mocker):
    sut, _, _ = self.make_sut()
    mocker.side_effect = Exception

    with pytest.raises(Exception):
      sut.auth(self.params)

  def test_4_should_call_HashComparer_with_correct_values(self):
    sut, hash_comparer_spy, load_account_by_email_repository_spy = self.make_sut()
    sut.auth(self.params)

    assert hash_comparer_spy.plain_password == self.params['password']
    assert hash_comparer_spy.hashed_password == load_account_by_email_repository_spy.result['password']
