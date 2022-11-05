from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.params import AddAccountParams
from src.domain.features import AddAccount

class TestAddAccount:
  def test_1_should_AddAccount_is_an_abstract_class(self):
    assert isabstract(AddAccount)

  @patch.multiple(AddAccount, __abstractmethods__=set())
  def test_2_should_AddAccount_raise_a_NotImplementedError_if_not_implemented(self):
    params: AddAccountParams = AddAccountParams(
      name='any_name',
      email='any_email@any.com',
      password='any_password'
    )
    addAccount: AddAccount = AddAccount()

    with pytest.raises(NotImplementedError, match='Should implement method: add'):
      addAccount.add(account=params)

  @patch.multiple(AddAccount, __abstractmethods__=set())
  def test_3_should_AddAccount_return_True_when_compare_objects(self):
    addAccount_1 = AddAccount()
    addAccount_2 = AddAccount()

    assert addAccount_1.__eq__
    assert addAccount_1 == addAccount_2
