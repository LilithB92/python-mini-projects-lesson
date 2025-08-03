def get_mask_card_number(card_number: int) -> str:
    """Функция  принимает на вход номер карты и возвращает ее маску."""
    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(card_account: int) -> str:
    """принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    card_account_str = str(card_account)
    return f"**{card_account_str[-4:]}"
