from dataclasses import dataclass
from typing import Any
from shutil import Error

@dataclass
class ServerError(Error):
  error: Any = None
  stack: Any = None

  def __post_init__(self):
    super().__init__('Internal Server Error')
