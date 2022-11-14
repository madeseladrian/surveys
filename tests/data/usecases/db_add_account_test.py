import pytest
from typing import Tuple
from unittest.mock import patch

from src.domain.params import AddAccountParams
from src.domain.features import AddAccount
from src.data.usecases import DbAddAccount

from ...domain.mocks import mock_add_account_params
from ..mocks import (
  AddAccountRepositorySpy,
  CheckAccountByEmailRepositorySpy,
  HasherSpy
)

class TestDbAddAccount:
  # SetUp
  params: AddAccountParams = mock_add_account_params()

  SutTypes = Tuple[
    AddAccount,
    AddAccountRepositorySpy,
    CheckAccountByEmailRepositorySpy,
    HasherSpy
  ]

  def make_sut(self) -> SutTypes:
    add_account_repository_spy = AddAccountRepositorySpy()
    check_account_by_email_repository_spy = CheckAccountByEmailRepositorySpy()
    hasher_spy = HasherSpy()
    sut: AddAccount = DbAddAccount(
      add_account_repository=add_account_repository_spy,
      check_account_by_email_repository=check_account_by_email_repository_spy,
      hasher=hasher_spy
    )
    return (
      sut,
      add_account_repository_spy,
      check_account_by_email_repository_spy,
      hasher_spy
    )

  # Success Tests

  def test_1_should_call_CheckAccountByEmailRepository_with_correct_email(self):
    sut, _, check_account_by_email_repository_spy, _ = self.make_sut()
    sut.add(self.params)

    assert check_account_by_email_repository_spy.email == self.params['email']

  def test_2_should_return_true_if_CheckAccountByEmailRepository_returns_false(self):
    sut, _, _, _ = self.make_sut()
    is_valid = sut.add(self.params)

    assert is_valid

  def test_3_should_return_false_if_CheckAccoutByEmailRepository_returns_true(self):
    sut, _, check_account_by_email_repository_spy, _ = self.make_sut()
    check_account_by_email_repository_spy.result = True
    is_valid = sut.add(self.params)

    assert not is_valid

  @patch('tests.data.mocks.CheckAccountByEmailRepositorySpy.check_by_email')
  def test_4_return_an_error_if_CheckAccountByEmailRepository_throws(self, mocker):
    sut, _, _, _ = self.make_sut()
    mocker.side_effect = Exception

    with pytest.raises(Exception):
      sut.add(self.params)

  def test_5_should_call_Hasher_with_correct_plaintext(self):
    sut, _, _, hasher_spy = self.make_sut()
    sut.add(self.params)

    assert hasher_spy.plaintext == self.params['password']

  @patch('tests.data.mocks.HasherSpy.hash')
  def test_6_return_an_error_if_Hasher_throws(self, mocker):
    sut, _, _, _ = self.make_sut()
    mocker.side_effect = Exception

    with pytest.raises(Exception):
      sut.add(self.params)

  def test_7_should_call_AddAccountRepository_with_correct_values(self):
    sut, add_account_repository_spy, _, hasher_spy = self.make_sut()
    self.params['password'] = hasher_spy.digest
    is_valid = sut.add(self.params)

    assert add_account_repository_spy.params == self.params
    assert is_valid

  def test_8_should_return_false_if_AddAccountRepository_returns_false(self):
    sut, add_account_repository_spy, _, _ = self.make_sut()
    add_account_repository_spy.result = False
    is_valid = sut.add(self.params)

    assert not is_valid

  @patch('tests.data.mocks.AddAccountRepositorySpy.add')
  def test_9_return_an_error_if_AddAccountRepository_throws(self, mocker):
    sut, _, _, _ = self.make_sut()
    mocker.side_effect = Exception

    with pytest.raises(Exception):
      sut.add(self.params)
