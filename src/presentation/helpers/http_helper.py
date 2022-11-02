from .http_response import HttpResponse

def bad_request(error: Exception) -> HttpResponse:
  return HttpResponse(status_code=400, body=error)

def forbidden(error: Exception) -> HttpResponse:
  return HttpResponse(status_code=403, body=error)
