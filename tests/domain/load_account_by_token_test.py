from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.features import LoadAccountByToken


class TestLoadAccountByToken:
    def test_1_should_LoadAccountByToken_is_an_abstract_class(self):
        assert isabstract(LoadAccountByToken)

    @patch.multiple(LoadAccountByToken, __abstractmethods__=set())
    def test_2_should_LoadAccountByToken_raise_a_NotImplementedError_if_not_implemented(self):
        load_account_by_token: LoadAccountByToken = LoadAccountByToken()

        with pytest.raises(NotImplementedError, match='Should implement method: load'):
            load_account_by_token.load(access_token='', role=None)
