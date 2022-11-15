from inspect import isabstract
import pytest
from unittest.mock import patch

from data.contracts.db.account import LoadAccountByEmailRepository


class TestLoadAccountByEmailRepository:
    def test_1_should_LoadAccountByEmailRepository_is_an_abstract_class(self):
        assert isabstract(LoadAccountByEmailRepository)

    @patch.multiple(LoadAccountByEmailRepository, __abstractmethods__=set())
    def test_2_should_LoadAccountByEmailRepository_raise_a_NotImplementedError_if_not_implemented(self):
        load_account_by_email_repository = LoadAccountByEmailRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: load_by_email'):
            load_account_by_email_repository.load_by_email(email='')
