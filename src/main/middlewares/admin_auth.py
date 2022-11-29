from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from ..factories.middlewares import auth_middleware_factory


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def admin_auth(token: str = Depends(oauth2_scheme)) -> str:
    middleware = auth_middleware_factory(role='admin')
    http_response = middleware.handle(token)
    body = http_response['body']
    return body['user_id']
