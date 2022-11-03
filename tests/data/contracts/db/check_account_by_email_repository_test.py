from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db import CheckAccountByEmailRepository

class TestCheckAccountByEmailRepository:
  def test_1_should_CheckAccountByEmailRepository_is_an_abstract_class(self):
    assert isabstract(CheckAccountByEmailRepository)

  @patch.multiple(CheckAccountByEmailRepository, __abstractmethods__=set())
  def test_2_should_CheckAccountByEmailRepository_raise_a_NotImplementedError_if_not_implemented(self):
    checkAccountByEmailRepository = CheckAccountByEmailRepository()

    with pytest.raises(NotImplementedError, match='Should implement method: check_by_email'):
      checkAccountByEmailRepository.check_by_email(email='')
