import pytest


@pytest.fixture(autouse=True)
def fixture3():
    print("I'm Fixture 3! And I'm called automatically!")


def test_autouse_fixture():
    ...
