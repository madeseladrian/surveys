from src.presentation.helpers import HttpResponse
from src.main.adapters import route_response_adapter
from .mocks import RouteResponseHelper


class TestRouteResponseAdapter:
    route_response = RouteResponseHelper()

    def test_1_should_adapter_return_correct_data_on_200(self):
        http_response: HttpResponse = {
            'status_code': 200,
            'body': True
        }

        assert route_response_adapter(http_response) == http_response

    def test_2_should_adapter_return_correct_data_on_201(self):
        http_response: HttpResponse = {
            'status_code': 201,
            'body': True
        }

        assert route_response_adapter(http_response) == http_response

    def test_3_should_adapter_return_no_data_on_204(self):
        http_response: HttpResponse = {
            'status_code': 204,
            'body': True
        }

        assert route_response_adapter(http_response) == http_response

    def test_4_should_adapter_return_a_bad_request_error(self):
        self.route_response.helper(
            status_code=400,
            detail='Bad Request Error'
        )

    def test_5_should_adapter_return_an_unauthorized_error(self):
        self.route_response.helper(
            status_code=401,
            detail='Unauthorized Error'
        )

    def test_6_should_adapter_return_a_forbbiden_error(self):
        self.route_response.helper(
            status_code=403,
            detail='Forbidden Error'
        )

    def test_7_should_adapter_return_a_server_error(self):
        self.route_response.helper(
            status_code=500,
            detail='Server Error'
        )

    def test_8_should_adapter_return_any_error(self):
        self.route_response.helper(
            status_code=422,
            detail='Server Error'
        )
