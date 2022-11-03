from inspect import isabstract

from src.data.contracts.db import AddAccountRepository

class TestController:
  def test_1_should_AddAccountRepository_is_an_abstract_class(self):
    assert isabstract(AddAccountRepository)
