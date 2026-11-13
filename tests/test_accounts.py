import pytest
from jsonschema import validate

from tests.schemas import ACCOUNT_SCHEMA


@pytest.mark.smoke
def test_accounts_list_is_not_empty(api):
    response = api.get_accounts()
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1
    accounts = response.json()
    assert isinstance(accounts, list) and accounts


@pytest.mark.regression
def test_every_account_matches_schema(api):
    for account in api.get_accounts().json():
        validate(instance=account, schema=ACCOUNT_SCHEMA)


@pytest.mark.regression
@pytest.mark.parametrize("account_id, currency", [(1, "USD"), (2, "EUR"), (3, "GEL")])
def test_account_by_id(api, account_id, currency):
    response = api.get_account(account_id)
    assert response.status_code == 200
    account = response.json()
    validate(instance=account, schema=ACCOUNT_SCHEMA)
    assert account["id"] == account_id
    assert account["currency"] == currency


@pytest.mark.regression
@pytest.mark.parametrize("account_id", [0, 999, "abc"])
def test_unknown_account_returns_404(api, account_id):
    assert api.get_account(account_id).status_code == 404


@pytest.mark.regression
def test_balance_is_never_negative(api):
    balances = [a["balance"] for a in api.get_accounts().json()]
    assert all(b >= 0 for b in balances), balances