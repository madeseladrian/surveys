from fastapi import HTTPException
import pytest

from src.main.adapters import route_response_adapter


class RouteResponseHelper:
    def helper(self, status_code: int, detail: str):
        response = {
            'status_code': status_code,
            'body': detail
        }

        with pytest.raises(HTTPException) as excinfo:
            route_response_adapter(response)
            assert isinstance(excinfo.value, HTTPException)
            assert excinfo.value.status_code == status_code
            assert excinfo.value.detail == detail
