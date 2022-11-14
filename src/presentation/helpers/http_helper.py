from typing import Any

from ..errors import ServerError
from .http_response import HttpResponse


def ok(data: Any) -> HttpResponse:
  return HttpResponse(status_code=200, body=data)

def add_account(data: Any) -> HttpResponse:
  return HttpResponse(status_code=201, body=data)

def bad_request(error: Exception) -> HttpResponse:
  return HttpResponse(status_code=400, body=error)

def forbidden(error: Exception) -> HttpResponse:
  return HttpResponse(status_code=403, body=error)

def server_error(error: Exception) -> HttpResponse:
  return HttpResponse(status_code=500, body=ServerError(error=error))
