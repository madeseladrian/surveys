from dataclasses import dataclass
from email_validator import validate_email

from ..validation.contracts import EmailValidator

@dataclass
class EmailValidatorAdapter(EmailValidator):

  def is_valid(self, email: str) -> bool:
    try:
      validation = validate_email(email=email, check_deliverability=True)
      return validation.email == email
    finally:
      return False
