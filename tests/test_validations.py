import pytest
from src.validations import process_bank_search
from src.validations import process_bank_operations

def test_import_process_bank_existed_search(transactions_list: list[dict])->None:
    assert process_bank_search(transactions_list,'EXECUTED') == transactions_list

def test_process_bank_not_existed_search(transactions_list: list[dict])->None:
    assert process_bank_search(transactions_list,'test') == [{}]

def test_process_bank_operations_with_existed_categories(transactions_list: list[dict])->None:
    assert process_bank_operations(transactions_list, ['Перевод организации', 'test']) == {'Перевод организации': 2}

def test_process_bank_operations_with_not_existed_categories(transactions_list:list[dict])->None:
    assert process_bank_operations(transactions_list, ['test1', 'test2']) == {}