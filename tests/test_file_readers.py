from io import StringIO
from typing import Any
from unittest import mock

import pandas as pd

import src
from src.file_readers import csv_reader
from src.file_readers import excel_reader


def test_csv_reader_not_exist_csv() -> None:
    assert csv_reader("not_exist_file") == [{}]


def test_excel_reader_not_exist_excel() -> None:
    assert excel_reader("not_exist_file") == [{}]


@mock.patch("builtins.open", new_callable=mock.mock_open)
def test_csv_reader(mock_open: Any) -> None:
    mock_csv_content = "header1;header2\nvalueA;valueB\nvalueC;valueD"
    mock_open.return_value = StringIO(mock_csv_content)

    result = csv_reader("dummy_path")

    assert result == [{"header1": "valueA", "header2": "valueB"}, {"header1": "valueC", "header2": "valueD"}]


@mock.patch("src.file_readers.pd.read_excel")
def test_your_function_with_mocked_excel(mock_read_excel: Any) -> None:
    mock_df = pd.DataFrame({"Column1": [1, 2], "Column2": ["A", "B"]})
    mock_read_excel.return_value = mock_df

    result = src.file_readers.excel_reader("some_file.xlsx")
    assert result == [{"Column1": 1, "Column2": "A"}, {"Column1": 2, "Column2": "B"}]
