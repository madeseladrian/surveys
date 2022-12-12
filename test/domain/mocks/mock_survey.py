from datetime import datetime
from faker import Faker
from typing import List

from src.domain.models import SurveyAnswerModel, SurveyModel


faker = Faker()

def mock_survey_model() -> SurveyModel:
    return SurveyModel(
        id=faker.uuid4(),
        question=faker.sentence(),
        answers=[
            SurveyAnswerModel(
                image=None,
                answer=faker.word()
            ),
            SurveyAnswerModel(
                image=faker.url(),
                answer=faker.word()
            ),
        ],
        date=datetime.now(),
        didAnswer=None
    )

def mock_survey_models() -> List[SurveyModel]:
    return [
        mock_survey_model(),
        mock_survey_model()
    ]
