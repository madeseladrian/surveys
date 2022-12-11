from unittest.mock import patch
import pytest

from src.infra.cryptography import BCryptAdapter


class TestBCryptAdapter:

    def make_sut(self) -> BCryptAdapter:
        return BCryptAdapter()

    # Hash

    @patch('src.infra.cryptography.BCryptAdapter.get_password_hash')
    def test_1_should_call_hash_with_correct_value(self, mocker):
        sut = self.make_sut()
        sut.get_password_hash('any_value')

        mocker.assert_called_once_with('any_value')

    def test_2_should_return_a_string_on_hash_success(self):
        sut = self.make_sut()
        hashed_password = sut.get_password_hash('any_value')

        assert isinstance(hashed_password, str)

    @patch('src.infra.cryptography.BCryptAdapter.get_password_hash')
    def test_3_should_return_a_valid_hash_on_hash_success(self, mocker):
        mocker.return_value = 'hashed'
        sut = self.make_sut()
        hashed_password = sut.get_password_hash('any_value')

        assert hashed_password == 'hashed'

    @patch('src.infra.cryptography.BCryptAdapter.get_password_hash')
    def test_4_should_throw_if_hash_throws(self, mocker):
        mocker.side_effect = Exception
        sut = self.make_sut()

        with pytest.raises(Exception):
            sut.get_password_hash('any_value')

    # HashComparer

    @patch('src.infra.cryptography.BCryptAdapter.verify_password')
    def test_5_should_call_verify_password_with_correct_values(self, mocker):
        sut = self.make_sut()
        sut.verify_password('any_value')

        mocker.assert_called_once_with('any_value')

    def test_6_should_should_return_true_on_hash_success(self):
        sut = self.make_sut()
        is_valid = sut.verify_password(
            plain_password='any_password',
            hashed_password='$2b$12$GPdEDnu7ZWAOm2jZphoEZejPoJ/fMfUoV/NXQh9A1mM4Tl3NmXir.'
        )

        assert is_valid

    def test_7_should_should_return_false_if_verify_password_fails(self):
        sut = self.make_sut()
        is_valid = sut.verify_password(
            plain_password='any_password',
            hashed_password='$2b$12$dSDB87pZc.WBs1OcUB1evujMAckGgRyRsQxf6ZvAmr2M6hg.uaLOy'
        )

        assert is_valid is False

    @patch('src.infra.cryptography.BCryptAdapter.verify_password')
    def test_8_should_throw_if_verify_password_throws(self, mocker):
        mocker.side_effect = Exception
        sut = self.make_sut()

        with pytest.raises(Exception):
            sut.verify_password('any_value')
