import os
from json import JSONDecodeError
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def amount_converter_to_rub(transaction: dict) -> Any:
    """
    Функция конвертации валюты из USD и EUR в рубли возвращает сумму транзакции (ключ amount) в рублях, если
    транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли
    :param transaction: транзакция
    :return:сумму транзакции в рублях
    """
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        if currency == "RUB":
            return amount
        else:
            url = "https://api.apilayer.com/exchangerates_data/convert"
            headers = {"apikey": api_key}
            payload = {"amount": amount, "from": currency, "to": "RUB"}
            response = requests.get(url, headers=headers, params=payload)
            if response.status_code == 200:
                return round(response.json()["result"], 2)
        return None
    except (JSONDecodeError, TypeError, KeyError, ValueError):
        return None
