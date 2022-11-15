from fastapi import FastAPI
from src.main.config import create_routes


class TestApp:
    app = FastAPI()
    create_routes(app)

    def test_1_should_calls_with_routes(self):
        routes = self.app.router.routes[4:]
        # path_routes = [route.__dict__['path'] for route in routes]

        assert len(routes) > 0
