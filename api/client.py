import requests


class TradingApi:
    """Small client for the accounts and orders API."""

    def __init__(self, base_url: str, timeout: float = 5):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def get_accounts(self):
        return self.session.get(self._url("accounts"), timeout=self.timeout)

    def get_account(self, account_id):
        return self.session.get(self._url(f"accounts/{account_id}"), timeout=self.timeout)

    def get_orders(self, **filters):
        return self.session.get(self._url("orders"), params=filters, timeout=self.timeout)

    def get_order(self, order_id):
        return self.session.get(self._url(f"orders/{order_id}"), timeout=self.timeout)

    def create_order(self, payload: dict):
        return self.session.post(self._url("orders"), json=payload, timeout=self.timeout)

    def update_order(self, order_id, changes: dict):
        return self.session.patch(self._url(f"orders/{order_id}"), json=changes, timeout=self.timeout)

    def delete_order(self, order_id):
        return self.session.delete(self._url(f"orders/{order_id}"), timeout=self.timeout)