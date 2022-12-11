from src.main.factories.middlewares import auth_middleware_factory
from src.presentation.middlewares import AuthMiddleware
from src.main.usecases import make_db_load_account_by_token


class TestMakeDbLoadAccountByToken:
    def test_1_should_call_AuthMiddleware_with_correct_values(self):
        auth_middleware = AuthMiddleware(
            load_account_by_token=make_db_load_account_by_token(),
            role=None
        )

        assert auth_middleware == auth_middleware_factory()
