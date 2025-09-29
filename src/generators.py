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


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None]:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди

    :param transactions: Список словарей, представляющих транзакции
    :return: описание каждой операции по очереди
    """
    descriptions = [trans["description"] for trans in transactions if trans["description"]]
    for description in descriptions:
        yield description
