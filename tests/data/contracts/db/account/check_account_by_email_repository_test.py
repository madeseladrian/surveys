from inspect import isabstract
import pytest
from unittest.mock import patch

from data.contracts.db.account import CheckAccountByEmailRepository


class TestCheckAccountByEmailRepository:
    def test_1_should_CheckAccountByEmailRepository_is_an_abstract_class(self):
        assert isabstract(CheckAccountByEmailRepository)

    @patch.multiple(CheckAccountByEmailRepository, __abstractmethods__=set())
    def test_2_should_CheckAccountByEmailRepository_raise_a_NotImplementedError_if_not_implemented(self):
        check_account_by_email_repository = CheckAccountByEmailRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: check_by_email'):
            check_account_by_email_repository.check_by_email(email='')
