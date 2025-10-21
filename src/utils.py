import json
import logging
import os
from json import JSONDecodeError
from typing import Any

directory_name = os.path.split(os.getcwd())[0]
log_path = os.path.join(directory_name, "logs", "utils.log")

logging.basicConfig(
    filename=log_path,
    format="%(asctime)s - %(filename)s - %(levelname)s:  %(message)s",
    filemode="w",
    level=logging.DEBUG,
    encoding="utf-8",
)


logger = logging.getLogger()


def read_json(filename: str) -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.

    :param filename: Путь до JSON-файла
    :return: возвращает список словарей с данными о финансовых транзакциях или пустой список
    """
    json_path = os.path.join(directory_name, "data", filename + ".json")
    try:
        logger.info("Открываем JSON-файл с данными о финансовых транзакциях")
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                logger.info("Возвращаем список словарей с данными о финансовых транзакциях")
                return json.load(f)
            except (AssertionError, JSONDecodeError) as ex:
                logger.error(f"Произошла ошибка: {ex}")
                return []
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []


if __name__ == "__main__":
    print(read_json("operations"))
