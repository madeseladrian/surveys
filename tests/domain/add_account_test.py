from abc import ABC, abstractmethod
from dataclasses import dataclass
from inspect import isabstract
from typing import TypedDict

class AddAccountParams(TypedDict):
  name: str
  email: str
  password: str

@dataclass
class AddAccount(ABC):

  @abstractmethod
  def add(self, account: AddAccountParams) -> bool:
    raise NotImplementedError('Should implement method: add')

class TestAddAccount:
  def test_1_should_AddAccount_is_an_abstract_class(self):
    assert isabstract(AddAccount)
