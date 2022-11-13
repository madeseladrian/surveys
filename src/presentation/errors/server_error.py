from dataclasses import dataclass
from typing import Any

@dataclass
class ServerError(Exception):
  error: Any = None
  stack: Any = None

  def __post_init__(self):
    super().__init__('Internal Server Error')
