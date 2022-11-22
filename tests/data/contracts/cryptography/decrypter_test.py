from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.cryptography import Decrypter


class TestDecrypter:
    def test_1_should_Decrypter_is_an_abstract_class(self):
        assert isabstract(Decrypter)

    @patch.multiple(Decrypter, __abstractmethods__=set())
    def test_2_should_Decrypter_raise_a_NotImplementedError_if_not_implemented(self):
        decrypter = Decrypter()

        with pytest.raises(NotImplementedError, match='Should implement method: decrypt'):
            decrypter.decrypt(token='')
