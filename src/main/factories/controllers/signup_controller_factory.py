from pymongo import MongoClient

from ....presentation.contracts import Controller
from ....presentation.controllers import SignUpController

from ...usecases import make_db_add_account, make_signup_validation
from ..decorators import log_controller_decorator_factory

def signup_controller_factory(client: MongoClient = None) -> Controller:
  controller = SignUpController(
    add_account=make_db_add_account(client=client),
    validation=make_signup_validation()
  )
  return log_controller_decorator_factory(
    client=client,
    controller=controller
  )
