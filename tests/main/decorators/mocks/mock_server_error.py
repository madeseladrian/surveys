from src.presentation.helpers import HttpResponse, server_error


def mock_server_error() -> HttpResponse:
    fake_error = Exception('any error')
    return server_error(fake_error)
