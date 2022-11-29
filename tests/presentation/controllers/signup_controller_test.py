from faker import Faker
from typing import Tuple
from unittest.mock import patch

from src.domain.params import AddAccountParams

from src.presentation.controllers import SignUpController
from src.presentation.errors import EmailInUseError, MissingParamError
from src.presentation.helpers import bad_request, forbidden, server_error

from ...domain.mocks import mock_add_account_params
from ..mocks import AuthenticationSpy, AddAccountSpy, ValidationSpy


class TestSignUpController:
    # SetUp
    faker = Faker()
    params: AddAccountParams = mock_add_account_params()

    SutTypes = Tuple[
        SignUpController,
        AddAccountSpy,
        AuthenticationSpy,
        ValidationSpy
    ]

    def make_sut(self) -> SutTypes:
        add_account_spy = AddAccountSpy()
        authentication_spy = AuthenticationSpy()
        validation_spy = ValidationSpy()
        sut = SignUpController(
          add_account=add_account_spy,
          authentication=authentication_spy,
          validation=validation_spy
        )

        return sut, add_account_spy, authentication_spy, validation_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, _, _, validation_spy = self.make_sut()
        request = self.params
        sut.handle(request=request)

        assert validation_spy.value == request

    def test_2_should_return_400_if_Validation_returns_an_error(self):
        sut, _, _, validation_spy = self.make_sut()
        validation_spy.error = MissingParamError(self.faker.word())
        http_response = sut.handle(self.params)

        assert http_response['status_code'] == 400
        assert http_response == bad_request(validation_spy.error)

    @patch('tests.presentation.mocks.ValidationSpy.validate')
    def test_3_should_return_500_if_Validation_throws(self, mocker):
        sut, _, _, _ = self.make_sut()
        exception = Exception()
        mocker.side_effect = exception
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 500
        assert http_response == server_error(error=exception)

    def test_4_should_call_AddAccount_with_correct_values(self):
        sut, add_account_spy, _, _ = self.make_sut()
        request = self.params
        sut.handle(request=request)

        assert add_account_spy.params == request

    def test_5_should_return_403_if_AddAccount_returns_false(self):
        sut, add_account_spy, _, _ = self.make_sut()
        add_account_spy.result = False
        http_response = sut.handle(self.params)

        assert http_response['status_code'] == 403
        assert http_response == forbidden(EmailInUseError())

    @patch('tests.presentation.mocks.AddAccountSpy.add')
    def test_6_should_return_500_if_AddAccount_throws(self, mocker):
        sut, _, _, _ = self.make_sut()
        exception = Exception()
        mocker.side_effect = exception
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 500
        assert http_response == server_error(error=exception)

    def test_7_should_call_Authentication_with_correct_values(self):
        sut, _, authentication_spy, _ = self.make_sut()
        request = self.params
        sut.handle(request=request)

        assert authentication_spy.params['email'] == request['email']
        assert authentication_spy.params['password'] == request['password']

    def test_8_should_return_200_if_valid_data_is_provided(self):
        sut, _, _, _ = self.make_sut()
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 200
        assert http_response.get('access_token', 'name')
