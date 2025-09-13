import pytest

from src.masks import get_mask_card_number


def test_get_mask_correct_card_number(card_number: int) -> None:
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_empty() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(int(""))


def test_get_mask_card_short_number(short_number: int) -> None:
    assert get_mask_card_number(short_number) == "Please, enter the correct card_number"


def test_get_mask_card_longer_number(long_number: int) -> None:
    assert get_mask_card_number(long_number) == "Please, enter the correct card_number"
