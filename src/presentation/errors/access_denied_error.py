from dataclasses import dataclass


@dataclass
class AccessDeniedError(Exception):

    def __post_init__(self):
        super().__init__('AccessDeniedError')
