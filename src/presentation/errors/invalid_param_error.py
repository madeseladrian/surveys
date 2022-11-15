from dataclasses import dataclass


@dataclass
class InvalidParamError(Exception):
    param_name: str

    def __post_init__(self):
        super().__init__(f'Invalid param: {self.param_name}')
