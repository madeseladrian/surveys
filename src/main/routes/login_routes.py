from fastapi import APIRouter, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ...presentation.params import LoginControllerRequest

from ..adapters import route_response_adapter
from ..docs.login_responses import responses
from ..factories.controllers import login_controller_factory
from ..models import LoginResponseModel


router = APIRouter(
    prefix='/api/login',
    tags=['Login']
)


@router.post(
    '/',
    responses=responses,
    status_code=status.HTTP_200_OK,
    response_model=LoginResponseModel
)
def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    request = LoginControllerRequest(
        email=user_credentials.username,
        password=user_credentials.password
    )
    controller = login_controller_factory()
    http_response = controller.handle(request)
    return route_response_adapter(http_response)
