from ....presentation.contracts import Controller
from ....presentation.controllers import LoginController

from ...usecases import make_db_authentication, make_login_validation
from ..decorators import log_controller_decorator_factory


@log_controller_decorator_factory
def login_controller_factory() -> Controller:
    return LoginController(
        authentication=make_db_authentication(),
        validation=make_login_validation()
    )
