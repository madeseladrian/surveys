from dataclasses import dataclass
from shutil import Error

@dataclass
class InvalidParamError(Error):
  paramName: str

  def __post_init__(self):
    super().__init__(f'Invalid param: {self.paramName}')
