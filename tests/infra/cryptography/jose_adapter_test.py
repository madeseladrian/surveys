from unittest.mock import patch
from src.infra.cryptography import JoseAdapter


class TestJoseAdapter:

    def make_sut(self) -> JoseAdapter:
        return JoseAdapter(
            algorithm='HS256',
            expire_in_days=1,
            key='any_key'
        )

    @patch('src.infra.cryptography.JoseAdapter.encrypt')
    def test_1_should_call_encrypt_with_correct_values(self, mocker):
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
