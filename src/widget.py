import re
from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Принимать один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером."""
    card_number_list = re.split(r"(\d+)", card_number)
    card_number_int = int(card_number_list[1])
    mask_number = ""

    if re.search("Счет", card_number):
        mask_number = get_mask_account(card_number_int)
    else:
        mask_number = get_mask_card_number(card_number_int)

    return f"{card_number_list[0]} {mask_number}"


def get_date(date_str: str) -> str:
    """принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'и возвращает строку
    с датой в формате 'ДД.ММ.ГГГГ' ('11.03.2024')"""

    format_with_time = "%Y-%m-%dT%H:%M:%S.%f"
    datetime_object = datetime.strptime(date_str, format_with_time)

    return f"{datetime_object.day}.{datetime_object.month}.{datetime_object.year}"
