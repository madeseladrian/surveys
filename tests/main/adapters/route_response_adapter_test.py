from fastapi import HTTPException
import pytest

from src.main.adapters import route_response_adapter
from src.presentation.helpers import HttpResponse

class TestRouteResponseAdapter:
  def test_1_should_adapter_return_correct_data(self):
    http_response: HttpResponse = {
      'status_code': 201,
      'body': True
    }

    assert route_response_adapter(http_response) == http_response

  def test_2_should_adapter_return_a_bad_request_error(self):
    http_response: HttpResponse = {
      'status_code': 400,
      'body': 'Bad Request Error'
    }
    with pytest.raises(HTTPException) as excinfo:
      route_response_adapter(http_response)

    assert isinstance(excinfo.value, HTTPException)
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == 'Bad Request Error'

  def test_3_should_adapter_return_a_forbbiden_error(self):
    http_response: HttpResponse = {
      'status_code': 403,
      'body': 'Forbidden Error'
    }
    with pytest.raises(HTTPException) as excinfo:
      route_response_adapter(http_response)

    assert isinstance(excinfo.value, HTTPException)
    assert excinfo.value.status_code == 403
    assert excinfo.value.detail == 'Forbidden Error'

  def test_4_should_adapter_return_a_server_error(self):
    http_response: HttpResponse = {
      'status_code': 500,
      'body': 'Server Error'
    }
    with pytest.raises(HTTPException) as excinfo:
      route_response_adapter(http_response)

    assert isinstance(excinfo.value, HTTPException)
    assert excinfo.value.status_code == 500
    assert excinfo.value.detail == 'Server Error'
