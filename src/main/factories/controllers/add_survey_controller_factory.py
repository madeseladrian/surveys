from ....presentation.contracts import Controller
from ....presentation.controllers import AddSurveyController

from ...usecases import make_db_add_survey, make_add_survey_validation
from ..decorators import log_controller_decorator_factory


@log_controller_decorator_factory
def add_survey_controller_factory() -> Controller:
    return AddSurveyController(
        add_survey=make_db_add_survey(),
        validation=make_add_survey_validation()
    )
