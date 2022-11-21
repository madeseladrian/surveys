from fastapi import HTTPException
import pytest

from src.presentation.helpers import HttpResponse
from src.main.adapters import route_response_adapter


class TestRouteResponseAdapter:

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

    def test_3_should_adapter_return_no_data_on_204(self):
        http_response: HttpResponse = {
            'status_code': 204,
            'body': True
        }

        assert route_response_adapter(http_response) == http_response

    def test_4_should_adapter_return_a_bad_request_error(self):
        http_response: HttpResponse = {
            'status_code': 400,
            'body': 'Bad Request Error'
        }

        with pytest.raises(HTTPException) as excinfo:
            route_response_adapter(http_response)

        assert isinstance(excinfo.value, HTTPException)
        assert excinfo.value.status_code == http_response['status_code']
        assert excinfo.value.detail == http_response['body']

    def test_5_should_adapter_return_an_unauthorized_error(self):
        http_response: HttpResponse = {
            'status_code': 401,
            'body': 'Unauthorized Error'
        }

        with pytest.raises(HTTPException) as excinfo:
            route_response_adapter(http_response)

        assert isinstance(excinfo.value, HTTPException)
        assert excinfo.value.status_code == http_response['status_code']
        assert excinfo.value.detail == http_response['body']

    def test_6_should_adapter_return_a_forbbiden_error(self):
        http_response: HttpResponse = {
            'status_code': 403,
            'body': 'Forbidden Error'
        }

        with pytest.raises(HTTPException) as excinfo:
            route_response_adapter(http_response)

        assert isinstance(excinfo.value, HTTPException)
        assert excinfo.value.status_code == http_response['status_code']
        assert excinfo.value.detail == http_response['body']

    def test_7_should_adapter_return_a_not_found_error(self):
        http_response = {
            'status_code': 404,
            'body': 'Not Found Error'
        }

        with pytest.raises(HTTPException) as excinfo:
            route_response_adapter(http_response)

        assert isinstance(excinfo.value, HTTPException)
        assert excinfo.value.status_code == http_response['status_code']
        assert excinfo.value.detail == http_response['body']

    def test_8_should_adapter_return_a_server_error(self):
        http_response = {
            'status_code': 500,
            'body': 'Server Error'
        }

        with pytest.raises(HTTPException) as excinfo:
            route_response_adapter(http_response)

        assert isinstance(excinfo.value, HTTPException)
        assert excinfo.value.status_code == http_response['status_code']
        assert excinfo.value.detail == http_response['body']

    def test_9_should_adapter_return_any_error(self):
        http_response = {
            'status_code': 422,
            'body': 'Validation Error'
        }

        with pytest.raises(HTTPException) as excinfo:
            route_response_adapter(http_response)

        assert isinstance(excinfo.value, HTTPException)
        assert excinfo.value.status_code == 500
        assert excinfo.value.detail == http_response['body']
