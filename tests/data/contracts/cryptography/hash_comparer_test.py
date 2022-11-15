from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.cryptography import HashComparer


class TestHashComparer:
    def test_1_should_HashComparer_is_an_abstract_class(self):
        assert isabstract(HashComparer)

    @patch.multiple(HashComparer, __abstractmethods__=set())
    def test_2_should_HashComparer_raise_a_NotImplementedError_if_not_implemented(self):
        hash_comparer = HashComparer()

        with pytest.raises(NotImplementedError, match='Should implement method: verify'):
            hash_comparer.verify(plain_password='', hashed_password='')
