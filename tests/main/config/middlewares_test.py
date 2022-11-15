from fastapi import FastAPI
from src.main.config import create_middlewares


class TestApp:
    app = FastAPI()
    create_middlewares(app)

    def test_1_should_calls_with_middlewares(self):
        middlewares = self.app.user_middleware[0].__dict__
        middlewares_options = middlewares['options']

        assert middlewares_options['allow_origins'] == ['*']
        assert middlewares_options['allow_credentials']
        assert middlewares_options['allow_methods'] == ['*']
        assert middlewares_options['allow_headers'] == ['*']
