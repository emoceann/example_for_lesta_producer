import pytest
from fastapi.testclient import TestClient

from src.server.app import create_app


@pytest.fixture(scope="session")
async def test_client():
    app = create_app()
    with TestClient(app=app, base_url="http://test") as client:
        yield client
