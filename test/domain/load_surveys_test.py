from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.features import LoadSurveys


class TestAddSurvey:
    def test_1_should_LoadSurveys_is_an_abstract_class(self):
        assert isabstract(LoadSurveys)

    @patch.multiple(LoadSurveys, __abstractmethods__=set())
    def test_2_should_LoadSurveys_raise_a_NotImplementedError_if_not_implemented(self):
        load_surveys = LoadSurveys()

        with pytest.raises(NotImplementedError, match='Should implement method: load'):
            load_surveys.load(account_id='any_id')
