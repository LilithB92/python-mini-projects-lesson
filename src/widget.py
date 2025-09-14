import re
from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """
  Функция замаскирует номер карты или счета
    :param card_number:  номер карты или счета
    :return: замаскированным номер карты или счета
    """
    card_number_list = re.split(r"(\d+)", card_number)
    card_number_int = int(card_number_list[1])
    if re.search("Счет", card_number):
        mask_number = get_mask_account(card_number_int)
    else:
        mask_number = get_mask_card_number(card_number_int)

    return f"{card_number_list[0]}{mask_number}"


def get_date(date_str: str) -> str:
    """
    Функция с датой в формате '2024-03-11T02:26:18.671407' отформатирует в дату формате 'ДД.ММ.ГГГГ' ('11.03.2024')
    :param date_str: дата в формате '2024-03-11T02:26:18.671407'
    :return: дата в формате 'ДД.ММ.ГГГГ'
    """

    format_with_time = "%Y-%m-%dT%H:%M:%S.%f"
    datetime_object = datetime.strptime(date_str, format_with_time)

    return f"{datetime_object.day}.{datetime_object.month}.{datetime_object.year}"

if __name__ == "__main__":
    result_1 = mask_account_card(int(input("Enter: ")))
    print(result_1)


