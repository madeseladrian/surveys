from fastapi import FastAPI
from ..routes import login_routes, signup_routes


def create_routes(app: FastAPI) -> None:
    app.include_router(signup_routes.router)
    app.include_router(login_routes.router)
