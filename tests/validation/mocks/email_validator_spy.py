from dataclasses import dataclass
from src.validation.contracts import EmailValidator


@dataclass
class EmailValidatorSpy(EmailValidator):
    email: str = ''
    is_email_valid: bool = True

    def is_valid(self, email: str) -> bool:
        self.email = email
        return self.is_email_valid
