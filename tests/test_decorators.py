import os
from datetime import datetime
from typing import Any

import pytest

from src.decorators import log


def test_double_decorator(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(3, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_invalid_datas_log(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def value_error_raiser() -> Any:
        raise ValueError("this is ValueError")

        captured = value_error_raiser()
        assert captured.err == "value_error_raiser error: ValueError. Inputs: (), {}"


def test_write_logs_datas_in_file() -> None:
    @log("hello")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(5, 4)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    directory_name = os.path.split(os.getcwd())[0]
    log_file = os.path.join(directory_name, "data", "hello.txt")
    with open(log_file) as f:
        assert f.read() == f"{current_date} my_function ok\n"


def test_write_logs_invalid_datas_in_file() -> None:
    @log("error_log")
    def value_error_raiser() -> Any:
        raise ValueError()

    value_error_raiser()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    directory_name = os.path.split(os.getcwd())[0]
    log_file = os.path.join(directory_name, "data", "error_log.txt")
    with open(log_file) as f:
        assert f.read() == current_date+(" value_error_raiser error: ValueError. Inputs: (), {}\n")
