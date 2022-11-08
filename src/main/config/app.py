from fastapi import FastAPI
from .middlewares import create_middlewares
from .routes import create_routes

def create_app(app: FastAPI) -> FastAPI:

  create_middlewares(app)
  create_routes(app)

  return app
