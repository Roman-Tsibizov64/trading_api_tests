ACCOUNT_SCHEMA = {
    "type": "object",
    "required": ["id", "owner", "currency", "balance", "leverage"],
    "properties": {
        "id": {"type": "integer"},
        "owner": {"type": "string", "minLength": 1},
        "currency": {"type": "string", "enum": ["USD", "EUR", "GEL"]},
        "balance": {"type": "number", "minimum": 0},
        "leverage": {"type": "integer", "minimum": 1},
    },
}

ORDER_SCHEMA = {
    "type": "object",
    "required": ["id", "accountId", "symbol", "side", "volume", "price", "status"],
    "properties": {
        "id": {"type": "integer"},
        "accountId": {"type": "integer"},
        "symbol": {"type": "string", "minLength": 6},
        "side": {"type": "string", "enum": ["buy", "sell"]},
        "volume": {"type": "number", "exclusiveMinimum": 0},
        "price": {"type": "number", "exclusiveMinimum": 0},
        "status": {"type": "string", "enum": ["new", "filled", "cancelled"]},
    },
}