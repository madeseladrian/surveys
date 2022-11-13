from faker import Faker
from typing import Tuple

from src.main.decorators import LogControllerDecorator
from .mocks import LogControllerSpy


class TestLogControllerDecorator:
  faker = Faker()
  request = {'status': 201, 'body': True}

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
    sut, log_controller_spy = self.make_sut()
    sut.handle(self.request)

    assert self.request['body'] == log_controller_spy.request['body']

  def test_2_should_return_the_same_result_of_the_controller(self):
    sut, log_controller_spy = self.make_sut()
    http_response = sut.handle(self.request)

    assert http_response == log_controller_spy.http_response
