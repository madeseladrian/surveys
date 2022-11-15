from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.features import Authentication
from src.domain.params import AuthenticationParams


class TestAuthentication:
    def test_1_should_Authentication_is_an_abstract_class(self):
        assert isabstract(Authentication)

    @patch.multiple(Authentication, __abstractmethods__=set())
    def test_2_should_Authentication_raise_a_NotImplementedError_if_not_implemented(self):
        params: AuthenticationParams = AuthenticationParams(
          email='any_email@any.com',
          password='any_password'
        )
        authentication: Authentication = Authentication()

        with pytest.raises(NotImplementedError, match='Should implement method: auth'):
            authentication.auth(authentication=params)
