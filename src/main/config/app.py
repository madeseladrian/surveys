from fastapi import FastAPI
from .middlewares import create_middlewares
from .routes import create_routes

def create_app() -> FastAPI:
  app = FastAPI(
    title='Surveys',
    version='1.0.0'
  )

  create_middlewares(app)
  create_routes(app)

  return app
