from faker import Faker

from src.presentation.errors import MissingParamError
from src.validation.validators import RequiredFieldValidation


class TestRequiredFieldValidation:
    faker = Faker()
    field_name: str = faker.word()

    def make_sut(self) -> RequiredFieldValidation:
        return RequiredFieldValidation(self.field_name)

    def test_1_should_return_a_MissingParamError_if_validation_fails(self):
        sut = self.make_sut()
        error = sut.validate({'invalidField': self.faker.word()})

        assert error == MissingParamError(self.field_name)

    def test_2_should_return_None_if_validation_succeeds(self):
        sut = self.make_sut()
        error = sut.validate({self.field_name: self.faker.word()})

        assert error is None
