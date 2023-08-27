from urllib.parse import urljoin

import names
import pytest
import requests

basic_url = "http://127.0.0.1:5000"
add_world_endpoint = urljoin(basic_url, "/addworld")
world_endpoint = urljoin(basic_url, "/world/{id}")


def check_world_state(id: int, world: dict | None):
    """Helper, GETs the world info and verifies its status"""
    get_response = requests.get(world_endpoint.format(id=id))
    assert get_response.ok
    if world:
        assert get_response.json()["world"][0] == world
    else:
        assert get_response.json()["world"] == []


@pytest.fixture
def new_world():
    """Creates a new and empty world and returns its params"""
    world_name = names.get_first_name()
    add_world_response = requests.post(add_world_endpoint, json={"name": world_name})
    return add_world_response.json()["world"][0]


def test_new_world(new_world):
    check_world_state(id=new_world["id"], world=new_world)


def test_put(new_world):
    new_world_name = names.get_first_name()
    response = requests.put(world_endpoint.format(id=new_world["id"]), json={"name": new_world_name})
    assert response.ok
    check_world_state(id=new_world["id"], world=response.json()["world"])


def test_delete(new_world):
    response = requests.delete(world_endpoint.format(id=new_world["id"]))
    assert response.status_code == 204
    check_world_state(id=new_world["id"], world=None)
