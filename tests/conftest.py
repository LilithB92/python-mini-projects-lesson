import pytest


@pytest.fixture
def empty_data() -> None:
    return None


@pytest.fixture
def card_number() -> int:
    return 7000792289606361


@pytest.fixture
def short_number() -> int:
    return 700079


@pytest.fixture
def long_number() -> int:
    return 736541084301358743054352633456
