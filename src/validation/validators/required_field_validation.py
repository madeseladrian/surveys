from dataclasses import dataclass
from typing import Any, Optional

from ...presentation.contracts import Validation
from ...presentation.errors import MissingParamError


@dataclass
class RequiredFieldValidation(Validation):
    field_name: str

    def validate(self, value: Any) -> Optional[Exception]:
        return None if value.get(self.field_name) \
            else MissingParamError(param_name=self.field_name)
