from fastapi import APIRouter, status

from ...presentation.params import SignUpControllerRequest

from ..adapters import route_response_adapter
from ..docs import responses
from ..factories.controllers import signup_controller_factory
from ..models import SignUpResponseModel

router = APIRouter(
  prefix='/signup',
  tags=['SignUp']
)


@router.post(
  '/',
  responses=responses,
  status_code=status.HTTP_201_CREATED,
  response_model=SignUpResponseModel
)
def create_user(request: SignUpControllerRequest):
  controller = signup_controller_factory()
  http_response = controller.handle(request)
  return route_response_adapter(http_response)
