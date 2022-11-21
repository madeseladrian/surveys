from src.presentation.middleware import AuthMiddleware
from src.presentation.helpers import forbidden
from src.presentation.errors import AccessDeniedError

from ..mocks import LoadAccountByTokenSpy


class TestAuthMiddleware:

    def make_sut(self, role: str = None) -> AuthMiddleware:
        load_account_by_token_spy = LoadAccountByTokenSpy()
        return AuthMiddleware(
            load_account_by_token=load_account_by_token_spy,
            role=role
        )

    def test_1_return_403_if_no_x_access_token_exists_in_headers(self):
        sut = self.make_sut()
        http_response = sut.handle({})

        assert http_response == forbidden(AccessDeniedError())
