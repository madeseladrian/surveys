from fastapi import APIRouter, Depends, status
from pymongo import MongoClient

from ...presentation.params import SignUpControllerRequest

from ..config.database import get_db
from ..adapters import route_response_adapter
from ..factories.controllers import signup_controller_factory
from ..models import SignUpResponseModel

router = APIRouter(
  prefix='/signup',
  tags=['SignUp']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=SignUpResponseModel)
def create_user(request: SignUpControllerRequest, client: MongoClient = Depends(get_db)):
  controller = signup_controller_factory(client=client)
  http_response = controller.handle(request)
  return route_response_adapter(http_response)
