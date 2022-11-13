from dataclasses import dataclass


@dataclass
class MissingParamError(Exception):
  param_name: str

  def __post_init__(self):
    super().__init__(f'Missing param: {self.param_name}')
