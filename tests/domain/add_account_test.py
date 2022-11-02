from abc import ABC, abstractmethod
from dataclasses import dataclass
from inspect import isabstract
import pytest
from typing import TypedDict
from unittest.mock import patch

class AddAccountParams(TypedDict):
  name: str
  email: str
  password: str

@dataclass
class AddAccount(ABC):

  @abstractmethod
  def add(self, account: AddAccountParams) -> bool:
    raise NotImplementedError('Should implement method: add')

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

    with pytest.raises(NotImplementedError) as exc_info:
      addAccount.add(account=params)
    assert exc_info.value.args[0] == 'Should implement method: add'

  @patch.multiple(AddAccount, __abstractmethods__=set())
  def test_3_should_AddAccount_return_True_when_compare_objects(self):
    addAccount_1 = AddAccount()
    addAccount_2 = AddAccount()

    assert addAccount_1.__eq__
    assert addAccount_1 == addAccount_2
