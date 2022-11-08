from fastapi import APIRouter

from ...presentation.params import SignUpControllerRequest
from ..factories.controllers import make_signup_controller

router = APIRouter(
  prefix='/signup',
  tags=['SignUp']
)

@router.post('/')
def create_user(request: SignUpControllerRequest):
  controller = make_signup_controller()
  return controller.handle(request)
