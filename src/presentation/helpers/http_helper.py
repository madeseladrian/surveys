from typing import Any

from ..errors import ServerError, UnauthorizedError
from .http_response import HttpResponse


def ok(data: Any) -> HttpResponse:
    return HttpResponse(status_code=200, body=data)

def add_account(data: Any) -> HttpResponse:
    return HttpResponse(status_code=201, body=data)

def no_content() -> HttpResponse:
    return HttpResponse(status_code=204, body=None)

def bad_request(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=400, body=error)

def unauthorized() -> HttpResponse:
    return HttpResponse(status_code=401, body=UnauthorizedError())

def forbidden(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=403, body=error)

def server_error(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=500, body=ServerError(error=error))
