from fastapi import FastAPI

from ..routes import signup_routes

def create_routes(app: FastAPI) -> None:
  app.include_router(signup_routes.router)
