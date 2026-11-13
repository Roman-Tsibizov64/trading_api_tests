import pytest
from jsonschema import validate

from tests.schemas import ORDER_SCHEMA


@pytest.mark.smoke
def test_orders_list_answers(api):
    response = api.get_orders()
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.regression
def test_created_order_matches_schema(new_order):
    validate(instance=new_order, schema=ORDER_SCHEMA)
    assert new_order["status"] == "new"


@pytest.mark.regression
def test_created_order_can_be_read(api, new_order):
    response = api.get_order(new_order["id"])
    assert response.status_code == 200
    assert response.json() == new_order


@pytest.mark.regression
def test_order_can_be_filled(api, new_order):
    response = api.update_order(new_order["id"], {"status": "filled"})
    assert response.status_code == 200
    assert api.get_order(new_order["id"]).json()["status"] == "filled"


@pytest.mark.regression
def test_deleted_order_is_gone(api, new_order):
    assert api.delete_order(new_order["id"]).status_code == 200
    assert api.get_order(new_order["id"]).status_code == 404


@pytest.mark.regression
@pytest.mark.parametrize("account_id", [1, 2])
def test_filter_by_account_returns_only_its_orders(api, new_order, account_id):
    orders = api.get_orders(accountId=account_id).json()
    assert all(o["accountId"] == account_id for o in orders), orders