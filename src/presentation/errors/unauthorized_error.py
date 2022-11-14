from dataclasses import dataclass

@dataclass
class UnauthorizedError(Exception):

  def __post_init__(self):
    super().__init__('UnauthorizedError')
