from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, None]:
    """
    Функция возвращает итератор, который поочередно выдает транзакции,
     где валюта операции соответствует заданной (например, USD).

    :param transactions: Список словарей, представляющих транзакции
    :param currency: валюта
    :return:итератор
    """
    filtered_trans = (
        trans
        for trans in transactions
        if trans is not None and trans["operationAmount"]["currency"]["name"] == currency
    )
    for transaction in filtered_trans:
        yield transaction
