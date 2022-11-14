from dataclasses import dataclass
from src.data.contracts.db.log import LogErrorRepository

@dataclass
class LogErrorRepositorySpy(LogErrorRepository):
  error: str = None

  def log_error(self, error: str) -> None:
    self.error = error
