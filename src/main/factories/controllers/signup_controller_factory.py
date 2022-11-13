from pymongo import MongoClient

from ....presentation.contracts import Controller
from ....presentation.controllers import SignUpController

from ...usecases import make_db_add_account, make_signup_validation


def signup_controller_factory(client: MongoClient = None) -> Controller:
  return SignUpController(
    add_account=make_db_add_account(client=client),
    validation=make_signup_validation()
  )
