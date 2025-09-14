from typing import Optional


def get_mask_card_number(card_number: int) -> Optional[str]:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    :param card_number: номер карты
    :return: маску карты по правилу XXXX XX** **** XXXX
    """
    if (len(str(card_number))) == 16:
        card_number_str = str(card_number)
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    return  None


def get_mask_account(card_account: int) -> Optional[str]:
    """
    Функция принимает на вход номер счета в виде 20 значного числа и возвращает маску номера
    :param card_account: номер счета
    :return: маску номера по правилу **XXXX
    """
    if (len(str(card_account))) == 20:
        card_account_str = str(card_account)
        return f"**{card_account_str[-4:]}"
    return None


if __name__ == "__main__":
    result_1 = get_mask_card_number(int(input("Enter: ")))
    print(result_1)
