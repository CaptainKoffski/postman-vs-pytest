import requests
from requests import codes


def test_two_plus_two():
    result = requests.post("http://127.0.0.1:8000/add", data={"a": 2, "b": 2})
    assert result.status_code == codes.OK
    assert result.json()["sum"] == 4
