from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.cryptography import Hasher


class TestHasher:
    def test_1_should_Hasher_is_an_abstract_class(self):
        assert isabstract(Hasher)

    @patch.multiple(Hasher, __abstractmethods__=set())
    def test_2_should_Hasher_raise_a_NotImplementedError_if_not_implemented(self):
        hasher = Hasher()

        with pytest.raises(NotImplementedError, match='Should implement method: get_password_hash'):
            hasher.get_password_hash(password='')
