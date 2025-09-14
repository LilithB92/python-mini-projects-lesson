import pytest


@pytest.fixture
def card_number() -> int:
    return 7000792289606361


@pytest.fixture
def short_number() -> int:
    return 700079


@pytest.fixture
def long_number() -> int:
    return 736541084301358743054352633456


@pytest.fixture
def card_account() -> int:
    return 73654108430135874305  # входной аргумент


@pytest.fixture
def some_string() -> str:
    return "Hello"


@pytest.fixture
def string_with_number() -> str:
    return "Maestro 1596837868"


@pytest.fixture
def dict_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]
