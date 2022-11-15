from inspect import isabstract
import pytest
from unittest.mock import patch

from data.contracts.db.account import UpdateAccessTokenRepository


class TestUpdateAccessTokenRepository:
    def test_1_should_UpdateAccessTokenRepository_is_an_abstract_class(self):
        assert isabstract(UpdateAccessTokenRepository)

    @patch.multiple(UpdateAccessTokenRepository, __abstractmethods__=set())
    def test_2_should_UpdateAccessTokenRepository_raise_a_NotImplementedError_if_not_implemented(self):
        update_access_token_repository = UpdateAccessTokenRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: update_access_token'):
            update_access_token_repository.update_access_token(id='', token='')
