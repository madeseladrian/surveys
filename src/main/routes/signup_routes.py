from fastapi import APIRouter, Depends
from pymongo import MongoClient

from ...presentation.params import SignUpControllerRequest
from ...presentation.helpers import HttpResponse

from ..factories.controllers import make_signup_controller
from ..config.database import get_db

router = APIRouter(
  prefix='/signup',
  tags=['SignUp']
)

@router.post('/', response_model=HttpResponse)
def create_user(request: SignUpControllerRequest, client: MongoClient = Depends(get_db)):
  controller = make_signup_controller(client=client)
  return controller.handle(request)
