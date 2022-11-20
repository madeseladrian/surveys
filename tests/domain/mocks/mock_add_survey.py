from faker import Faker
from src.domain.params import AddSurveyParams, SurveyAnswerModel


faker = Faker()

def mock_add_survey_params() -> AddSurveyParams:
    return AddSurveyParams(
        question=faker.sentence(),
        answers=[SurveyAnswerModel(
            image=faker.image_url(),
            answer=faker.word()
        )]
    )
