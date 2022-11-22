from src.presentation.params import AuthMiddlewareRequest

def mock_auth_middleware_params() -> AuthMiddlewareRequest:
    return AuthMiddlewareRequest(
        access_token='any_token'
    )
