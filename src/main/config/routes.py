from fastapi import FastAPI
from ..routes import login_routes, survey_routes


def create_routes(app: FastAPI) -> None:
    app.include_router(login_routes.router)
    app.include_router(survey_routes.router)
