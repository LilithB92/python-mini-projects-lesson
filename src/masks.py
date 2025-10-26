import logging
import os
from typing import Optional

directory_name = os.path.split(os.getcwd())[0]
log_path = os.path.join(directory_name, "logs", "masks.log")

logging.basicConfig(
    filename=log_path,
    format="%(asctime)s - %(filename)s - %(levelname)s:  %(message)s",
    filemode="w",
    level=logging.DEBUG,
    encoding="utf-8",
)


logger = logging.getLogger()


def get_mask_card_number(card_number: int) -> Optional[str]:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    :param card_number: номер карты
    :return: маску карты по правилу XXXX XX** **** XXXX
    """
    if (len(str(card_number))) == 16:
        card_number_str = str(card_number)
        logger.info(
            f"Возвращаем маску карты: {card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        )
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    logger.warning("Длина номер карты не корректно")
    return None


def get_mask_account(card_account: int) -> Optional[str]:
    """
    Функция принимает на вход номер счета в виде 20 значного числа и возвращает маску номера
    :param card_account: номер счета
    :return: маску номера по правилу **XXXX
    """
    if (len(str(card_account))) == 20:
        card_account_str = str(card_account)
        logger.info(f"Возвращаем маску номера счета: **{card_account_str[-4:]}")
        return f"**{card_account_str[-4:]}"
    logger.warning("Длина номер карты не корректно")
    return None


if __name__ == "__main__":
    get_mask_account(2123122144)
    get_mask_account(12345678912345436789)
