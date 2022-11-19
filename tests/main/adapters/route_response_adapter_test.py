from fastapi import HTTPException
import pytest

from src.presentation.helpers import HttpResponse
from src.main.adapters import route_response_adapter


class TestRouteResponseAdapter:
    def _route_response_helper(self, http_response, status_code: int, detail: str) -> None:
        with pytest.raises(HTTPException) as excinfo:
            route_response_adapter(http_response)
            assert isinstance(excinfo.value, HTTPException)
            assert excinfo.value.status_code == status_code
            assert excinfo.value.detail == detail

    def test_1_should_adapter_return_correct_data_on_200(self):
        http_response: HttpResponse = {
            'status_code': 200,
            'body': True
        }

        assert route_response_adapter(http_response) == http_response

    def test_2_should_adapter_return_correct_data_on_201(self):
        http_response: HttpResponse = {
            'status_code': 201,
            'body': True
        }

        assert route_response_adapter(http_response) == http_response

    def test_3_should_adapter_return_a_bad_request_error(self):
        http_response = {
            'status_code': 400,
            'body': 'Bad Request Error'
        }

        self._route_response_helper(
            http_response=http_response,
            status_code=400,
            detail='Bad Request Error'
        )

    def test_4_should_adapter_return_an_unauthorized_error(self):
        http_response = {
            'status_code': 401,
            'body': 'Unauthorized Error'
        }

        self._route_response_helper(
            http_response=http_response,
            status_code=401,
            detail='Unauthorized Error'
        )

    def test_5_should_adapter_return_a_forbbiden_error(self):
        http_response = {
            'status_code': 403,
            'body': 'Forbidden Error'
        }

        self._route_response_helper(
            http_response=http_response,
            status_code=403,
            detail='Forbidden Error'
        )

    def test_6_should_adapter_return_a_server_error(self):
        http_response = {
            'status_code': 500,
            'body': 'Server Error'
        }

        self._route_response_helper(
            http_response=http_response,
            status_code=500,
            detail='Server Error'
        )

    def test_7_should_adapter_return_any_error(self):
        http_response: HttpResponse = {
            'status_code': 422,
            'body': 'Server Error'
        }

        self._route_response_helper(
            http_response=http_response,
            status_code=422,
            detail='Server Error'
        )
