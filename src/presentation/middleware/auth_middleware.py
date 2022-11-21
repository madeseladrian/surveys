from dataclasses import dataclass
from typing import Optional

from ...domain.features import LoadAccountByToken
from ..contracts import Middleware
from ..errors import AccessDeniedError
from ..helpers import forbidden, HttpResponse
from ..params import AuthMiddlewareRequest


@dataclass
class AuthMiddleware(Middleware):
    load_account_by_token: LoadAccountByToken
    role: Optional[str]

    def handle(self, request: AuthMiddlewareRequest) -> HttpResponse:
        return forbidden(AccessDeniedError())
