import pytest
from starlette.testclient import TestClient

from tests.constants.log_post_request_examples import log_request_successful, log_request_unsuccessful


@pytest.mark.asyncio(scope="session")
class TestProducerLogEndpoint:
    async def test_success_request(self, test_client: TestClient):
        resp = test_client.post(
            "/producer/log",
            json=log_request_successful
        )
        assert resp.status_code == 200

    async def test_unsuccess_request(self, test_client: TestClient):
        resp = test_client.post(
            "/producer/log",
            json=log_request_unsuccessful
        )
        assert resp.status_code == 422
