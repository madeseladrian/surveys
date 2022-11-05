from unittest.mock import patch
import pytest

from src.infra.cryptography import BCryptAdapter

class TestBCryptAdapter:

  bcryptAdapter = BCryptAdapter()

  @patch('src.infra.cryptography.BCryptAdapter.hash')
  def test_1_should_call_hash_with_correct_value(self, mocker):
    self.bcryptAdapter.hash('any_value')

    mocker.assert_called_once_with('any_value')

  @patch('src.infra.cryptography.BCryptAdapter.hash')
  def test_2_should_return_a_valid_hash_on_hash_success(self, mocker):
    mocker.return_value = 'hashed'
    hashed_password = self.bcryptAdapter.hash('any_value')

    assert hashed_password == 'hashed'

  @patch('src.infra.cryptography.BCryptAdapter.hash')
  def test_3_should_throw_if_hash_throws(self, mocker):
    mocker.side_effect = Exception

    with pytest.raises(Exception):
      self.bcryptAdapter.hash('any_value')
