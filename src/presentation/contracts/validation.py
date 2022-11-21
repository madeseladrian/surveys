from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class Validation(ABC):

    @abstractmethod
    def validate(self, value: Any) -> Optional[Exception]:
        raise NotImplementedError('Should implement method: validate')
