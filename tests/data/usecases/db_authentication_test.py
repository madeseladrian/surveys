import pytest
from typing import Tuple
from unittest.mock import patch

from src.domain.params import AuthenticationParams
from src.domain.features import Authentication
from src.data.usecases import DbAuthentication

from ...domain.mocks import mock_authentication_params
from ..mocks import (
  EncrypterSpy,
  HashComparerSpy,
  LoadAccountByEmailRepositorySpy
)


class TestDbAuthentication:
  # SetUp
  params: AuthenticationParams = mock_authentication_params()

  SutTypes = Tuple[
    Authentication,
    EncrypterSpy,
    HashComparerSpy,
    LoadAccountByEmailRepositorySpy
  ]

  def make_sut(self) -> SutTypes:
    encrypter_spy = EncrypterSpy()
    hash_comparer_spy = HashComparerSpy()
    load_account_by_email_repository_spy = LoadAccountByEmailRepositorySpy()
    sut: DbAuthentication = DbAuthentication(
      encrypter=encrypter_spy,
      hash_comparer=hash_comparer_spy,
      loadAccount_by_email_repository=load_account_by_email_repository_spy
    )
    return (
      sut,
      encrypter_spy,
      hash_comparer_spy,
      load_account_by_email_repository_spy
    )

  def test_1_should_call_LoadAccountByEmailRepository_with_correct_email(self):
    sut, _, _, load_account_by_email_repository_spy = self.make_sut()
    sut.auth(self.params)

    assert load_account_by_email_repository_spy.email == self.params['email']

  def test_2_should_return_None_if_LoadAccountByEmailRepository_returns_None(self):
    sut, _, _, load_account_by_email_repository_spy = self.make_sut()
    load_account_by_email_repository_spy.result = None
    authentication_model = sut.auth(self.params)

    assert authentication_model is None

  @patch('tests.data.mocks.LoadAccountByEmailRepositorySpy.load_by_email')
  def test_3_should_return_an_error_if_LoadAccountByEmailRepository_throws(self, mocker):
    sut, _, _, _ = self.make_sut()
    mocker.side_effect = Exception

    with pytest.raises(Exception):
      sut.auth(self.params)

  def test_4_should_call_HashComparer_with_correct_values(self):
    sut, _, hash_comparer_spy, load_account_by_email_repository_spy = self.make_sut()
    sut.auth(self.params)

    assert hash_comparer_spy.plain_password == self.params['password']
    assert hash_comparer_spy.hashed_password == load_account_by_email_repository_spy.result['password']

  def test_5_should_return_None_if_HashComparer_returns_false(self):
    sut, _, hash_comparer_spy, _ = self.make_sut()
    hash_comparer_spy.is_valid = False
    authentication_model = sut.auth(self.params)

    assert authentication_model is None

  @patch('tests.data.mocks.HashComparerSpy.verify')
  def test_6_should_return_an_error_if_HashComparer_throws(self, mocker):
    sut, _, _, _ = self.make_sut()
    mocker.side_effect = Exception

    with pytest.raises(Exception):
      sut.auth(self.params)

  def test_7_should_call_Encrypter_with_correct_plain_password(self):
    sut, encrypter_spy, _, load_account_by_email_repository_spy = self.make_sut()
    sut.auth(self.params)

    assert encrypter_spy.plain_password == load_account_by_email_repository_spy.result['id']
