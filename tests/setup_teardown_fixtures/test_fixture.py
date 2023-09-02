import names
import pytest
import requests


@pytest.fixture
def new_world_id(basic_url):
    """Adds a new world, returns its ID, and deletes it when testing is complete"""
    response = requests.post(f"{basic_url}/addworld", json={"name": "whatever"})
    worldid = response.json()["world"][0]["id"]
    yield worldid
    requests.delete(f"{basic_url}/world/{worldid}")


def test_add_castle(
    basic_url,  # this is a fixture call
    new_world_id,  # and this is too
):
    # you can see how basic_url and new_world_id fixtures
    # are used in the f-string below
    url = f"{basic_url}/world/{new_world_id}/castle"
    name = names.get_first_name()
    response = requests.post(url, json={"name": name})
    assert response.ok
    assert name == response.json()["castle"][0]["name"]
