from dataclasses import dataclass
from shutil import Error

@dataclass
class MissingParamError(Error):
  param_name: str

  def __post_init__(self):
    super().__init__(f'Missing param: {self.param_name}')
