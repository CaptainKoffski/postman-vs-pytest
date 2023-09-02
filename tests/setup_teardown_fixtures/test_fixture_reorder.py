import pytest


@pytest.fixture
def fixture1():
    print("I'm Fixture 1 !")


@pytest.fixture
def fixture2():
    print("I'm Fixture 2 !")


def test_fixture_order(fixture1, fixture2):
    ...
