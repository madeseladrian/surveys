from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from ..helpers import HttpResponse


@dataclass
class Controller(ABC):

    @abstractmethod
    def handle(self, request: Any) -> HttpResponse:
        raise NotImplementedError('Should implement method: handle')
