from dataclasses import dataclass

from ....data.contracts.db.survey import AddSurveyRepository
from ....data.params import AddSurveyRepositoryParams
from .mongo_helper import mongohelper


@dataclass
class SurveyMongoRepository(AddSurveyRepository):

    def add(self, data: AddSurveyRepositoryParams) -> None:
        survey_collection = mongohelper.get_collection(collection='surveys')
        survey_collection.insert_one(dict(data))
