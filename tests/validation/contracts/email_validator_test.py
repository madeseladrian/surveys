from inspect import isabstract
import pytest
from unittest.mock import patch

from src.validation.contracts import EmailValidator


class TestAddAccount:
    def test_1_should_EmailValidator_is_an_abstract_class(self):
        assert isabstract(EmailValidator)

    @patch.multiple(EmailValidator, __abstractmethods__=set())
    def test_2_should_EmailValidator_raise_a_NotImplementedError_if_not_implemented(self):
        email_validator = EmailValidator()

        with pytest.raises(NotImplementedError, match='Should implement method: is_valid'):
            email_validator.is_valid(email='any_email@any.com')
