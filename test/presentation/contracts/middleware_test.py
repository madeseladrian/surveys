from inspect import isabstract
import pytest
from unittest.mock import patch

from src.presentation.contracts import Middleware


class TestMiddleware:
    def test_1_should_Middleware_is_an_abstract_class(self):
        assert isabstract(Middleware)

    @patch.multiple(Middleware, __abstractmethods__=set())
    def test_2_should_Middleware_raise_a_NotImplementedError_if_not_implemented(self):
        middleware = Middleware()

        with pytest.raises(NotImplementedError, match='Should implement method: handle'):
            middleware.handle(request='')
