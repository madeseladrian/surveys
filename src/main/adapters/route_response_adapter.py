from fastapi import HTTPException, status
from typing import Any

from ...presentation.helpers import HttpResponse


def route_response_adapter(http_response: HttpResponse) -> Any:
    status_code: int = http_response['status_code']

    match status_code:
        case 200: return http_response
        case 201: return http_response
        case 400: raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST,
          detail=f"{http_response['body']}"
        )
        case 401: raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail=f"{http_response['body']}"
        )
        case 403: raise HTTPException(
          status_code=status.HTTP_403_FORBIDDEN,
          detail=f"{http_response['body']}"
        )
        case 500: raise HTTPException(
          status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
          detail=f"{http_response['body']}"
        )
        case _: raise HTTPException(
          status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
          detail=f"{http_response['body']}"
        )
