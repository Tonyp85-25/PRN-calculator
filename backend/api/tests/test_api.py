import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.db.session import get_db
from api.db.base_class import Base
from main import include_router

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI()
include_router(app)
Base.metadata.create_all(bind=engine)
app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


class CalculateApiTest(unittest.TestCase):
    def setUp(self):
        self.client = client

    def test_send_add(self):
        response = self.client.post("/calculate", json={"expression": "2 2 +"})
        self.assertEqual(200, response.status_code)
        self.assertEqual("4.0", response.json()["result"])

    def test_no_operators_sent(self):
        response = self.client.post("/calculate", json={"expression": "2 8"})
        self.assertEqual(422, response.status_code)

    def test_no_numbers_sent(self):
        response = self.client.post("/calculate", json={"expression": "* +"})
        self.assertEqual(422, response.status_code)
