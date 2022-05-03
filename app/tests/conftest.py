from typing import Dict, Generator

import pytest
from app.core.settings import settings
from app.db.session import SessionLocal
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


@pytest.fixture(scope="session")
def db():
    yield SessionLocal()
