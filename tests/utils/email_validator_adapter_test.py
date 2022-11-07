from src.utils import EmailValidatorAdapter

class TestEmailValidatorAdapter:

  def make_sut(self) -> EmailValidatorAdapter:
    return EmailValidatorAdapter()

  def test_1_should_return_false_if_email_validator_returns_false(self):
    sut = self.make_sut()
    is_valid = sut.is_valid('invalid_email')

    assert is_valid is False
