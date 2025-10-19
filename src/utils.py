import json
import os
from json import JSONDecodeError


def json_reader(filename: str) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.

    :param filename: Путь до JSON-файла
    :return: возвращает список словарей с данными о финансовых транзакциях или пустой список
    """
    directory_name = os.path.split(os.getcwd())[0]
    json_path = os.path.join(directory_name, "data", filename + ".json")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                return []
            except (JSONDecodeError, TypeError, KeyError, ValueError):
                return []
    except FileNotFoundError:
        return []



