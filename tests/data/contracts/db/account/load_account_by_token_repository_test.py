from inspect import isabstract
import pytest
from unittest.mock import patch

from data.contracts.db.account import LoadAccountByTokenRepository


class TestLoadAccountByEmailRepository:
    def test_1_should_LoadAccountByTokenRepository_is_an_abstract_class(self):
        assert isabstract(LoadAccountByTokenRepository)

    @patch.multiple(LoadAccountByTokenRepository, __abstractmethods__=set())
    def test_2_should_LoadAccountByTokenRepository_raise_a_NotImplementedError_if_not_implemented(self):
        load_account_by_token_repository = LoadAccountByTokenRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: load_by_token'):
            load_account_by_token_repository.load_by_token(token='', role=None)
