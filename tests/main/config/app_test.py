from fastapi import FastAPI
from src.main.config import create_app

class TestApp:
  def test_1_should_create_app_is_instance_of_fastapi(self):
    assert isinstance(create_app(), FastAPI)
