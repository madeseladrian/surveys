from inspect import isabstract
import pytest
from unittest.mock import patch

from src.presentation.contracts import Validation


class TestValidation:
    def test_1_should_Validation_is_an_abstract_class(self):
        assert isabstract(Validation)

    @patch.multiple(Validation, __abstractmethods__=set())
    def test_2_should_Validation_raise_a_NotImplementedError_if_not_implemented(self):
        """ The set __abstractmethods__ attribute to be an empty set you will
        be able to instantiate abstract class.

        PEP 3119:
          If the resulting __abstractmethods__ set is non-empty, the
          class is considered abstract, and attempts to instantiate
          it will raise TypeError
        """

        validation = Validation()

        with pytest.raises(NotImplementedError, match='Should implement method: validate'):
            validation.validate(value='')
