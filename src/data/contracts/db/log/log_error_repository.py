from abc import ABC, abstractmethod

class LogErrorRepository(ABC):

  @abstractmethod
  def log_error(self, stack: str) -> None:
    raise NotImplementedError('Should implement method: log_error')
