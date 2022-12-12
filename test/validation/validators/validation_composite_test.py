from faker import Faker
from typing import Any, List, Tuple

from src.presentation.contracts.validation import Validation
from src.presentation.errors import MissingParamError
from src.validation.validators import ValidationComposite

from ...presentation.mocks.validation import ValidationSpy


class TestValidationComposite:
    faker = Faker()
    field: str = faker.word()

    SutTypes = Tuple[ValidationComposite, List[Validation]]

    def _validate_composite_helper(self, validation_spies: Any, sut: Any, validation_spy: int):
        validation_spies[1].error = MissingParamError(self.field)
        error = sut.validate({self.field: self.faker.word()})
        assert error == validation_spies[validation_spy].error

    def make_sut(self) -> SutTypes:
        validation_spies: List[Validation] = [
          ValidationSpy(),
          ValidationSpy()
        ]
        sut = ValidationComposite(validation_spies)
        return sut, validation_spies

    def test_1_should_return_an_error_if_any_validation_fails(self):
        sut, validation_spies = self.make_sut()
        self._validate_composite_helper(validation_spies, sut, 1)

    def test_2_should_return_the_first_error_if_more_then_one_validation_fails(self):
        sut, validation_spies = self.make_sut()
        validation_spies[0].error = Exception
        self._validate_composite_helper(validation_spies, sut, 0)

    def test_3_should_return_None_if_validation_succeds(self):
        sut, _ = self.make_sut()
        error = sut.validate({self.field: self.faker.word()})

        assert error is None
