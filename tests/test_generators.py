import pytest

from src.generators import filter_by_currency
from src.generators import transaction_descriptions


def test_filter_transaction_by_currency(transactions_list: list) -> None:
    each_transaction = filter_by_currency(transactions_list, "USD")
    assert next(each_transaction) == {
        "id": 939719456,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(each_transaction) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    with pytest.raises(StopIteration):
        next(each_transaction)


def test_transaction_descriptions(transactions_list: list) -> None:
    description = transaction_descriptions(transactions_list)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"

    with pytest.raises(StopIteration):
        next(description)


def test_transaction_descriptions_without_description() -> None:
    with pytest.raises(KeyError):
        next(transaction_descriptions([{}]))
