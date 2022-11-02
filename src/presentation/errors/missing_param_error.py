from dataclasses import dataclass

@dataclass
class MissingParamError(Exception):
  paramName: str

  def __post_init__(self):
    super().__init__(f'Missing param: {self.paramName}')
