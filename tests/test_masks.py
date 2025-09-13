import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_correct_card_number(card_number: int) -> None:
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_empty() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(int(""))


def test_get_mask_card_account_short_number(short_number: int) -> None:
    assert get_mask_card_number(short_number) == "Please, enter the correct card_number"
    assert get_mask_account(short_number) == "Please, enter the correct card_account"


def test_get_mask_card_account_longer_number(long_number: int) -> None:
    assert get_mask_card_number(long_number) == "Please, enter the correct card_number"
    assert get_mask_account(long_number) == "Please, enter the correct card_account"


def test_get_correct_mask_account(card_account: int) -> None:
    assert get_mask_account(card_account) == "**4305"


def test_get_mask_card_account_empty() -> None:
    with pytest.raises(ValueError):
        get_mask_account(int(""))
