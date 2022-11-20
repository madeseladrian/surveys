from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

@dataclass
class Validation(ABC):

    @abstractmethod
    def validate(self, value: Any) -> Exception:
        raise NotImplementedError('Should implement method: validate')
