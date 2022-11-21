from ...domain.features import AddSurvey
from ...data.usecases import DbAddSurvey
from ...infra.db.mongodb import SurveyMongoRepository


def make_db_add_survey() -> AddSurvey:
    survey_mongo_repository = SurveyMongoRepository()
    return DbAddSurvey(survey_mongo_repository)
