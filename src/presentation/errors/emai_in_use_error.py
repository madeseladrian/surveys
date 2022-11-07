from dataclasses import dataclass
from shutil import Error

@dataclass
class EmailInUseError(Error):
  def __post_init__(self):
    super().__init__('The received email is already in use')
