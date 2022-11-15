from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from src.domain.params import AuthenticationParams, AuthenticationResult

@dataclass
class Authentication(ABC):

  @abstractmethod
  def auth(self, authentication: AuthenticationParams) -> Optional[AuthenticationResult]:
    raise NotImplementedError('Should implement method: auth')
