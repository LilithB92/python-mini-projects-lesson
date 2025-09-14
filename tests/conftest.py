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
