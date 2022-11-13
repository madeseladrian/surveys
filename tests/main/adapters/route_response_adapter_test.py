from src.main.adapters import route_response_adapter
from src.presentation.helpers import HttpResponse

class TestRouteResponseAdapter:
  def test_1_should_adapter_return_correct_data(self):
    http_response: HttpResponse = {
      'status_code': 201,
      'body': True
    }

    assert route_response_adapter(http_response) == http_response
