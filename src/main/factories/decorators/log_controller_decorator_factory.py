from pymongo import MongoClient

from ....presentation.contracts import Controller
from ....infra.db.mongodb import LogMongoRepository
from ...decorators import LogControllerDecorator

def log_controller_decorator_factory(client: MongoClient, controller: Controller):
  log_mongo_repository = LogMongoRepository(client=client)

  return LogControllerDecorator(
    controller=controller,
    log_error_repository=log_mongo_repository
  )
