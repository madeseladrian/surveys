from fastapi import APIRouter, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ...presentation.params import (
    LoginControllerRequest,
    SignUpControllerRequest
)
from ..adapters import route_response_adapter
from ..docs import login_responses, sign_up_responses
from ..factories.controllers import (
    login_controller_factory,
    signup_controller_factory
)
from ..models import LoginResponseModel


router = APIRouter(
    tags=['Login']
)

@router.post(
    '/signup/',
    responses=sign_up_responses,
    status_code=status.HTTP_200_OK,
    response_model=LoginResponseModel
)
def create_user(request: SignUpControllerRequest):
    controller = signup_controller_factory()
    http_response = controller.handle(request)
    adapter = route_response_adapter(http_response)
    body = adapter.get('body')
    return {**body, 'token_type': 'bearer'}


@router.post(
    '/login/',
    responses=login_responses,
    status_code=status.HTTP_200_OK,
    response_model=LoginResponseModel
)
def login(request: OAuth2PasswordRequestForm = Depends()):
    controller = login_controller_factory()
    http_response = controller.handle(LoginControllerRequest(
        email=request.username,
        password=request.password
    ))
    adapter = route_response_adapter(http_response)
    body = adapter.get('body')
    return {**body, 'token_type': 'bearer'}
