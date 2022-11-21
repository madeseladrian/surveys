from inspect import isabstract
import pytest
from unittest.mock import patch

from data.contracts.db.survey import AddSurveyRepository


class TestAddSurveyRepository:
    def test_1_should_AddSurveyRepository_is_an_abstract_class(self):
        assert isabstract(AddSurveyRepository)

    @patch.multiple(AddSurveyRepository, __abstractmethods__=set())
    def test_2_should_AddSurveyRepository_raise_a_NotImplementedError_if_not_implemented(self):
        add_survey_repository = AddSurveyRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: add'):
            add_survey_repository.add(data={})
