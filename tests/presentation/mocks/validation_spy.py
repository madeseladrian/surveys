from typing import Any, Optional
from src.presentation.contracts import Validation


class ValidationSpy(Validation):
    error: Optional[Exception] = None
    value: Any

    def validate(self, value: Any) -> Exception:
        self.value = value
        return self.error
