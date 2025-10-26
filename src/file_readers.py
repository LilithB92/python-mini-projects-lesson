import os
from typing import Any

import pandas as pd

project_path = os.path.split(os.getcwd())[0]


def csv_reader(filename: str) -> list[dict[Any, Any]]:
    """
    Функция считывает финансовых операций из CSV

    :param filename:путь к файлу CSV
    :return:список словарей с транзакциями.
    """
    csv_file = os.path.join(project_path, "data", filename + ".csv")
    try:
        csv_data = pd.read_csv(csv_file, encoding="utf-8", sep=";")
        try:
            return csv_data.to_dict(orient="records")
        except (AttributeError, ValueError, TypeError):
            return [{}]
    except FileNotFoundError:
        return [{}]


def excel_reader(filename: str) -> list[dict[Any, Any]]:
    """
    Функция считывает финансовых операций из Excel

    :param filename: путь к файлу Excel
    :return:список словарей с транзакциями.
    """
    excel_file = os.path.join(project_path, "data", filename + ".xlsx")
    try:
        excel_data = pd.read_excel(excel_file)
        try:
            return excel_data.to_dict(orient="records")
        except (AttributeError, ValueError, TypeError):
            return [{}]
    except FileNotFoundError:
        return [{}]


if __name__ == "__main__":
    print(csv_reader("djs"))
    print(excel_reader("fs"))
