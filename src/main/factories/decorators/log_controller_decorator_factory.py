from ....infra.db.mongodb import LogMongoRepository
from ...decorators import LogControllerDecorator

def log_controller_decorator_factory(controller_function):
  def wrapper_controller(*args, **kwargs):
    controller = controller_function(*args, **kwargs)
    log_mongo_repository = LogMongoRepository(*args, **kwargs)

    return LogControllerDecorator(
      controller=controller,
      log_error_repository=log_mongo_repository
    )

  return wrapper_controller
