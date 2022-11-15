from dataclasses import dataclass


@dataclass
class EmailInUseError(Exception):
    def __post_init__(self):
        super().__init__('The received email is already in use')
