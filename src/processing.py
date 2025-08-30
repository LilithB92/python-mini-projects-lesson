def filter_by_state(dicts_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
        Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED')."""
    return list(filter(lambda x: x.get("state") == state, dicts_list))


def sort_by_date(data: list, reverse: bool = True) -> list:
    """Функция возвращает новый список словарей, отсортированный по дате (date).
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
