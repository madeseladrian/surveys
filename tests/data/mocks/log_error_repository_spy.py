from dataclasses import dataclass
from src.data.contracts.db.log import LogErrorRepository

@dataclass
class LogErrorRepositorySpy(LogErrorRepository):
  stack: str = None

  def log_error(self, stack: str) -> None:
    self.stack = stack
