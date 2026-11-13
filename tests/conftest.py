import os

import pytest

from api.client import TradingApi

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")


@pytest.fixture(scope="session")
def api():
    return TradingApi(BASE_URL)


@pytest.fixture
def new_order(api):
    """Creates an order before the test and removes it after, so tests stay independent."""
    payload = {
        "accountId": 2,
        "symbol": "GBPUSD",
        "side": "sell",
        "volume": 0.5,
        "price": 1.27,
        "status": "new",
    }
    response = api.create_order(payload)
    assert response.status_code == 201, response.text
    order = response.json()
    yield order
    api.delete_order(order["id"])