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


def card_number_generator(start: int, stop: int) -> Generator[str, None]:
    """
    Функция который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.

    :param start: Начальное значения для генерации диапазона номеров
    :param stop: конечное значения для генерации диапазона номеров
    :return: номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты
    """
    if start < stop:
        card_numbers = [str(x).zfill(16) for x in range(start, stop + 1)]
        for card_number in card_numbers:
            formated_card_number = ""
            for i in range(0, 16, 4):
                formated_card_number += card_number[i : i + 4] + " "
            yield formated_card_number.rstrip()
