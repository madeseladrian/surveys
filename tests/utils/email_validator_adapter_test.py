from src.utils import EmailValidatorAdapter

class TestEmailValidatorAdapter:

  def make_sut(self) -> EmailValidatorAdapter:
    return EmailValidatorAdapter()

  def test_1_should_return_false_if_email_validator_returns_false(self):
    sut = self.make_sut()
    is_valid = sut.is_valid('invalid.email')

    assert is_valid is False

  def test_2_should_return_true_if_validator_returns_true(self):
    sut = self.make_sut()
    is_valid = sut.is_valid('mades@gmail.com')

    assert is_valid
