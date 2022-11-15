from abc import ABC, abstractmethod
from typing import Any


class LogErrorRepository(ABC):

    @abstractmethod
    def log_error(self, error: Any) -> None:
        raise NotImplementedError('Should implement method: log_error')
