from inspect import isabstract
from src.validation.contracts import EmailValidator

class TestAddAccount:
  def test_1_should_EmailValidator_is_an_abstract_class(self):
    assert isabstract(EmailValidator)
