from fastapi import FastAPI
from .config import create_app

app = FastAPI(
  title='Surveys',
  version='1.0.0'
)

create_app(app=app)
