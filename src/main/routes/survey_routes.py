from fastapi import APIRouter, status

from ...presentation.params import AddSurveyControllerRequest
from ..adapters import route_response_adapter
from ..docs import sign_up_responses
from ..factories.controllers import add_survey_controller_factory


router = APIRouter(
    tags=['Enquete'],
    prefix='/surveys'
)

@router.post(
    '/',
    responses=sign_up_responses,
    status_code=status.HTTP_204_NO_CONTENT
)
def add_survey(request: AddSurveyControllerRequest):
    controller = add_survey_controller_factory()
    http_response = controller.handle(request)
    return route_response_adapter(http_response)
