from ....presentation.contracts import Controller
from ....presentation.controllers import SignUpController

from ...usecases import make_db_add_account, make_signup_validation

def make_signup_controller() -> Controller:
  return SignUpController(
    add_account=make_db_add_account(),
    validation=make_signup_validation()
  )
