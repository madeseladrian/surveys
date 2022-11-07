from unittest.mock import patch
from src.utils import EmailValidatorAdapter

class TestEmailValidatorAdapter:

  def make_sut(self) -> EmailValidatorAdapter:
    return EmailValidatorAdapter()

  @patch('src.utils.EmailValidatorAdapter.is_valid')
  def test_1_should_call_validator_with_correct_email(self, mocker):
    sut = self.make_sut()
    sut.is_valid('any_email')

    mocker.assert_called_once_with('any_email')

  def test_2_should_return_false_if_email_validator_returns_false(self):
    sut = self.make_sut()
    is_valid = sut.is_valid('invalid.email')

    assert is_valid is False

  def test_3_should_return_true_if_validator_returns_true(self):
    sut = self.make_sut()
    is_valid = sut.is_valid('mades@gmail.com')

    assert is_valid
