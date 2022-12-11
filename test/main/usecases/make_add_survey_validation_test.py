from src.validation.validators import (
    ValidationComposite,
    RequiredFieldValidation
)
from src.main.usecases import make_add_survey_validation


class TestMakeAddSurveyValidation:
    def test_1_should_call_ValidationComposite_with_all_validations(self):
        validations = [
            RequiredFieldValidation(field_name=field)
            for field in ['question', 'answers']
        ]
        validation_composite = ValidationComposite(validations)

        assert validation_composite == make_add_survey_validation()
