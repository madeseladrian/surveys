from datetime import datetime
from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.features import AddSurvey
from src.domain.params import AddSurveyParams, SurveyAnswerModel


class TestAddSurvey:
    def test_1_should_AddSurvey_is_an_abstract_class(self):
        assert isabstract(AddSurvey)

    @patch.multiple(AddSurvey, __abstractmethods__=set())
    def test_2_should_AddSurvey_raise_a_NotImplementedError_if_not_implemented(self):
        params = AddSurveyParams(
            id='any_id',
            question='any_question',
            answers=[SurveyAnswerModel(
                image='any_image',
                answer='other_answer'
            )],
            date=datetime.now()
        )
        add_survey = AddSurvey()

        with pytest.raises(NotImplementedError, match='Should implement method: add'):
            add_survey.add(data=params)
