from typing import Any, TypedDict


class HttpResponse(TypedDict):
    status_code: int
    body: Any
