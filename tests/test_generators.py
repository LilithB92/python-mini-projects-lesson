import pytest

from src.generators import card_number_generator
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


def test_filter_invalid(transactions_list: list) -> None:
    each_transaction = filter_by_currency(transactions_list, "USD")
    next(each_transaction)
    next(each_transaction)
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


def test_card_number_generator() -> None:
    card_number = card_number_generator(1, 5)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"

    with pytest.raises(StopIteration):
        next(card_number)


@pytest.mark.parametrize(
    "start,stop,expected",
    [
        (7, 8, "0000 0000 0000 0007"),
        (2, 4, "0000 0000 0000 0002"),
    ],
)
def test_card_number_generator_in_one_assertion(start: int, stop: int, expected: str) -> None:
    assert next(card_number_generator(start, stop)) == expected


def test_card_number_generator_invalid_start_bigger() -> None:
    with pytest.raises(StopIteration):
        next(card_number_generator(5, 1))
