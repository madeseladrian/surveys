from faker import Faker
from src.domain.params import AddAccountParams


faker = Faker()

def mock_add_account_params() -> AddAccountParams:
    return AddAccountParams(
      name=faker.name(),
      email=faker.email(),
      password=faker.password()
    )
