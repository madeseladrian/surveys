from inspect import isabstract

from src.data.contracts.cryptography import Hasher

class TestController:
  def test_1_should_Hasher_is_an_abstract_class(self):
    assert isabstract(Hasher)
