import pytest

from src.widget import mask_account_card

@pytest.mark.parametrize("card,expected",
                          [("Maestro 1596837868705199","Maestro 1596 83** **** 5199"),
                           ("Счет 64686473678894779589","Счет **9589"),
                           ("Visa Platinum 7000792289606361","Visa Platinum 7000 79** **** 6361"),
                           ("Счет 73654108430135874305","Счет **4305"),
                           ("MasterCard 7158300734726758","MasterCard 7158 30** **** 6758"),
                           ("Visa Classic 6831982476737658","Visa Classic 6831 98** **** 7658"),
                           ("Visa Gold 5999414228426353","Visa Gold 5999 41** **** 6353")])
def test_mask_account_card(card,expected):
    assert mask_account_card(card) == expected