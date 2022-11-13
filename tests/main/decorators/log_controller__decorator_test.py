from faker import Faker
from typing import Tuple

from src.main.decorators import LogControllerDecorator
from .mocks import LogControllerSpy


class TestLogControllerDecorator:
  faker = Faker()

  SutTypes = Tuple[
    LogControllerDecorator,
    LogControllerSpy
  ]

  def make_sut(self) -> SutTypes:
    log_controller_spy = LogControllerSpy()
    sut = LogControllerDecorator(
      controller=log_controller_spy
    )

    return sut, log_controller_spy

  def test_1_should_call_controller_handle(self):
    request = {'status': 201, 'body': True}

    sut, log_controller_spy = self.make_sut()
    sut.handle(request)

    assert log_controller_spy.request['body'] == request['body']
