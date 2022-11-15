from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_username: str
    database_password: str

    class Config:
        env_file = '.env'

settings = Settings()

uri: str = f'mongodb://\
{settings.database_hostname}:\
{settings.database_port}'
