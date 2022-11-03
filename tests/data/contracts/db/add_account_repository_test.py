from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db import AddAccountRepository

class TestAddAccountRepository:
  def test_1_should_AddAccountRepository_is_an_abstract_class(self):
    assert isabstract(AddAccountRepository)

  @patch.multiple(AddAccountRepository, __abstractmethods__=set())
  def test_2_should_AddAccountRepository_raise_a_NotImplementedError_if_not_implemented(self):
    addAccountRepository = AddAccountRepository()

    with pytest.raises(NotImplementedError, match='Should implement method: add'):
      addAccountRepository.add(data={})
