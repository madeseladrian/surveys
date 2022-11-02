from abc import ABC, abstractmethod
from dataclasses import dataclass
from shutil import Error
from typing import Any, Optional

@dataclass
class Validation(ABC):

  @abstractmethod
  def validate(self, value: Any) -> Optional[Error]:
    raise NotImplementedError('Should implement method: validate')
