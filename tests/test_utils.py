from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from src.utils import read_json


def test_read_json_filename_not_exist() -> None:
    assert read_json("not_exist_file") == []


def test_read_json_decode_error() -> None:
    mock = mock_open()
    with patch("builtins.open", mock):
        with open("output.json", "w") as f:
            f.write("{Some data}")
        with pytest.raises(AssertionError):
            assert read_json("output")
