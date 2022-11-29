from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db.log import LogErrorRepository


class TestAddAccount:
    def test_1_should_LogErrorRepository_is_an_abstract_class(self):
        assert isabstract(LogErrorRepository)

    @patch.multiple(LogErrorRepository, __abstractmethods__=set())
    def test_2_should_LogErrorRepository_raise_a_NotImplementedError_if_not_implemented(self):
        log_error_repository = LogErrorRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: log_error'):
            log_error_repository.log_error(error='any error')
