def filter_by_state(dicts_list: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    :param dicts_list: Список словарей
    :param state: ключа state (по умолчанию 'EXECUTED')
    :return: новый список словарей
    """
    return list(filter(lambda x: x.get("state") == state, dicts_list))


def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Функция список словарей отсортированный по дате (date).
    :param data: Список словарей
    :param reverse: задающий порядок сортировки (по умолчанию — убывание)
    :return:  новый список словарей, отсортированный по дате (date)
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
