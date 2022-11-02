from inspect import isabstract

from src.presentation.contracts import Controller

class TestController:
  def test_1_should_Controller_is_an_abstract_class(self):
    assert isabstract(Controller)
