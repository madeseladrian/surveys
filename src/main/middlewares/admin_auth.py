from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from ...presentation.params import AuthMiddlewareRequest
from ..adapters import route_response_adapter
from ..factories.middlewares import auth_middleware_factory


oauth2_login = OAuth2PasswordBearer(tokenUrl='login')

def admin_auth(token: str = Depends(oauth2_login)) -> str:
    print(token)
    middleware = auth_middleware_factory(role='admin')
    http_response = middleware.handle(AuthMiddlewareRequest(access_token=token))
    adapter = route_response_adapter(http_response)
    body = adapter.get('body')
    return body.get('user_id')
