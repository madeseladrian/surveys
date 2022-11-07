from dataclasses import dataclass
from typing import Any
from shutil import Error

@dataclass
class ServerError(Error):
  error: Any = None

  def __post_init__(self):
    super().__init__(f'Error: {self.error}')
