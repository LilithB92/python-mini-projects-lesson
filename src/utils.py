import json
import os
from json import JSONDecodeError
from typing import Any


def read_json(filename: str) -> Any:
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
                return json.load(f)
            except (AssertionError, JSONDecodeError):
                return []
    except FileNotFoundError:
        return []


print(read_json("operations"))
