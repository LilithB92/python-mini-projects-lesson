from typing import Any
from unittest.mock import patch

import pytest

from src.external_api import amount_converter_to_rub


def test_amount_convert_to_rub(transaction: dict) -> None:
    assert amount_converter_to_rub(transaction) == 31957.58


def test_amount_convert_none() -> None:
    with pytest.raises(AssertionError):
        assert amount_converter_to_rub(
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                }
        )


@patch("src.external_api.requests.get")
def test_amount_convert_from_usd_currency(mocked_get: Any, transaction_with_usd_currency: dict) -> None:
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {"result": 345.234}
    result = amount_converter_to_rub(transaction_with_usd_currency)
    assert result == 345.23


@patch("src.external_api.requests.get")
def test_amount_convert_with_error_status_code(mocked_get: Any, transaction_with_usd_currency: dict) -> None:
    mocked_get.return_value.status_code = 400
    mocked_get.return_value.json.return_value = {"result": 345.234}
    result = amount_converter_to_rub(transaction_with_usd_currency)
    assert result is None
