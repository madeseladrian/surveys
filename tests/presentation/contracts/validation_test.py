from inspect import isabstract
from src.presentation.contracts import Validation

class TestValidation:
  def test_1_should_Validation_is_an_abstract_class(self):
    assert isabstract(Validation)
