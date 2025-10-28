import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция возвращает те банковские операции в которых есть строка поиска

    :param data: список словарей с данными о банковских операциях
    :param search: строка поиска,
    :return:возвращать список словарей, у которых в описании есть данная строка, или [{}]
    """
    pattern = rf"{search}"
    results = [trans for trans in data if re.search(pattern, str(trans), flags=re.IGNORECASE)]
    if results:
        return results
    else:
        return [{}]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция подсчитывает количество банковских операций по категориям

    :param data: список словарей с данными о банковских операциях
    :param categories:Список строк с названиями категорий
    :return:Словарь, где ключи - это названия категорий, а значения - количество операций в каждой категории.
    """
    trnas_categories = [trans["description"] for trans in data if trans["description"] in categories]
    return dict(Counter(trnas_categories))
