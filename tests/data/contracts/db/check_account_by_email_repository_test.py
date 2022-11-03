from inspect import isabstract

from src.data.contracts.db import CheckAccountByEmailRepository

class TestCheckAccountByEmailRepository:
  def test_1_should_CheckAccountByEmailRepository_is_an_abstract_class(self):
    assert isabstract(CheckAccountByEmailRepository)
