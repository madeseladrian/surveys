from faker import Faker
from typing import Tuple

from src.main.decorators import LogControllerDecorator

from ...data.mocks import LogErrorRepositorySpy
from .mocks import LogControllerSpy, mock_server_error


class TestLogControllerDecorator:
    faker = Faker()
    request = {'status': 201, 'body': True}

    SutTypes = Tuple[
      LogControllerDecorator,
      LogControllerSpy,
      LogErrorRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        log_controller_spy = LogControllerSpy()
        log_error_repository = LogErrorRepositorySpy()
        sut = LogControllerDecorator(
          controller=log_controller_spy,
          log_error_repository=log_error_repository
        )

        return sut, log_controller_spy, log_error_repository

    def test_1_should_call_controller_handle(self):
        sut, log_controller_spy, _ = self.make_sut()
        sut.handle(self.request)

        assert self.request['body'] == log_controller_spy.request['body']

    def test_2_should_return_the_same_result_of_the_controller(self):
        sut, log_controller_spy, _ = self.make_sut()
        http_response = sut.handle(self.request)

        assert http_response == log_controller_spy.http_response

    def test_3_should_call_LogErrorRepository_with_correct_error_if_controller_returns_a_server_error(self):
        sut, log_controller_spy, log_error_repository_spy = self.make_sut()
        server_error = mock_server_error()
        log_controller_spy.http_response = server_error
        sut.handle(self.request)

        assert log_error_repository_spy.error == server_error['body'].error
