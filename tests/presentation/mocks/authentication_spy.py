from faker import Faker

from src.domain.features import Authentication
from src.domain.params import AuthenticationParams, AuthenticationResult


faker = Faker()

class AuthenticationSpy(Authentication):
    params: AuthenticationParams
    result: AuthenticationResult = AuthenticationResult(
      access_token=faker.uuid4(),
      name=faker.name()
    )

    def auth(self, params: AuthenticationParams) -> AuthenticationResult:
        self.params = params
        return self.result
