from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.cryptography import Encrypter

class TestEncrypter:
    def test_1_should_Encrypter_is_an_abstract_class(self):
        assert isabstract(Encrypter)

    @patch.multiple(Encrypter, __abstractmethods__=set())
    def test_2_should_Encrypter_raise_a_NotImplementedError_if_not_implemented(self):
        encrypter = Encrypter()

        with pytest.raises(NotImplementedError, match='Should implement method: encrypt'):
            encrypter.encrypt(user_id='')
