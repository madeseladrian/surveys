from unittest.mock import patch
from src.infra import BCryptAdapter

class TestBCryptAdapter:

  def make_sut(self) -> BCryptAdapter:
    return BCryptAdapter()

  @patch('src.infra.BCryptAdapter.hash')
  def test_1_should_call_hash_with_correct_value(self, mocker):
    sut = self.make_sut()
    sut.hash('any_value')

    mocker.assert_called_once_with('any_value')
