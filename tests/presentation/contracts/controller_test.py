from inspect import isabstract
import pytest
from unittest.mock import patch

from src.presentation.contracts import Controller


class TestController:
    def test_1_should_Controller_is_an_abstract_class(self):
        assert isabstract(Controller)

    @patch.multiple(Controller, __abstractmethods__=set())
    def test_2_should_Controller_raise_a_NotImplementedError_if_not_implemented(self):
        controller = Controller()

        with pytest.raises(NotImplementedError, match='Should implement method: handle'):
            controller.handle(request='')
