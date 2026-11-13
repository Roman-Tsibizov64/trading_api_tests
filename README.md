# Trading API tests

![API tests](https://github.com/YOUR_LOGIN/trading_api_tests/actions/workflows/api_tests.yml/badge.svg)

API autotests in Python (pytest + requests) for a small trading service with accounts and orders.
The test stand runs in Docker Compose; GitHub Actions starts it and runs all tests on every push and every morning.

## What is inside

| Part | What it does |
| --- | --- |
| `compose.yaml` | test stand: REST API (json-server) in Docker |
| `stand/db.json` | test data: 3 accounts and 1 order |
| `api/client.py` | API client class, tests never build URLs by hand |
| `tests/` | 16 pytest tests: accounts, orders, JSON schemas, fixtures |
| `postman/` | the same checks as a Postman collection |
| `.github/workflows/api_tests.yml` | CI: stand in Docker, pytest, HTML report as an artifact |

## What is checked

* status codes 200, 201, 404 (including invalid ids: 0, 999, text)
* response time under 1 second
* account and order responses match JSON schemas
* balance is never negative, currency is one of USD, EUR, GEL
* full order life cycle: create, read, fill, delete, make sure it is gone
* filter by account returns only that account's orders
* each test creates its own order with a fixture and removes it, so tests do not depend on each other

## How to run locally

1. Start Docker Desktop, then in the project folder: `docker compose up -d`
2. `pip install -r requirements.txt`
3. `pytest` (only quick checks: `pytest -m smoke`)
4. HTML report: `pytest --html=reports/report.html --self-contained-html`
5. Stop the stand: `docker compose down`

In GitHub the report of every run is in the Actions tab, block Artifacts, file `pytest_report`.