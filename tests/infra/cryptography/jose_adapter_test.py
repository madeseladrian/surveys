from unittest.mock import patch
import pytest

from src.infra.cryptography import JoseAdapter


class TestJoseAdapter:

    def make_sut(self) -> JoseAdapter:
        return JoseAdapter(
            algorithm='HS256',
            expire_in_days=1,
            key='any_key'
        )

    @patch('src.infra.cryptography.JoseAdapter.encrypt')
    def test_1_should_call_encrypt_with_correct_value(self, mocker):
        sut = self.make_sut()
        sut.encrypt('any_value')

        mocker.assert_called_once_with('any_value')

    def test_2_should_return_a_string_on_encrypt_success(self):
        sut = self.make_sut()
        encrypted_user_id = sut.encrypt('any_value')

        assert isinstance(encrypted_user_id, str)

    @patch('src.infra.cryptography.JoseAdapter.encrypt')
    def test_3_should_return_a_valid_token_on_encrypt_success(self, mocker):
        mocker.return_value = 'any_token'
        sut = self.make_sut()
        encrypted_user_id = sut.encrypt('any_id')

        assert encrypted_user_id == 'any_token'

    @patch('src.infra.cryptography.JoseAdapter.encrypt')
    def test_4_should_throw_if_encrypt_throws(self, mocker):
        mocker.side_effect = Exception
        sut = self.make_sut()

        with pytest.raises(Exception):
            sut.encrypt('any_id')

    @patch('src.infra.cryptography.JoseAdapter.decrypt')
    def test_5_should_call_decrypt_with_correct_value(self, mocker):
        sut = self.make_sut()
        sut.decrypt('any_value')

        mocker.assert_called_once_with('any_value')
