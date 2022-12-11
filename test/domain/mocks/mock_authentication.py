from faker import Faker
from src.domain.params import AuthenticationParams


faker = Faker()

def mock_authentication_params() -> AuthenticationParams:
    return AuthenticationParams(
        email=faker.email(),
        password=faker.password()
    )
