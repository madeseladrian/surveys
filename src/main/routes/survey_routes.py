from fastapi import APIRouter, Depends, status

from ...presentation.params import AddSurveyControllerRequest
from ..adapters import route_response_adapter
from ..docs import sign_up_responses
from ..factories.controllers import add_survey_controller_factory
from ..middlewares import admin_auth


router = APIRouter(
    tags=['Enquete'],
    prefix='/surveys'
)

@router.post(
    '/',
    responses=sign_up_responses,
    status_code=status.HTTP_204_NO_CONTENT
)
def add_survey(request: AddSurveyControllerRequest, user_id: str = Depends(admin_auth)):
    controller = add_survey_controller_factory()
    http_response = controller.handle(request)
    return route_response_adapter(http_response)
