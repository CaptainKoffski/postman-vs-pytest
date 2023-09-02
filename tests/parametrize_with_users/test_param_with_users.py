import pytest
import requests as requests
from pydantic.v1 import BaseModel


class Castle(BaseModel):
    """Model to show we can use custom types as field types too"""

    name: str
    ...


class Goomba(BaseModel):
    """Model for our users"""

    login: str
    password: str
    castle: Castle  # here it is, our custom field type
    ...

    def sign_up(self):
        """Wow, we can add methods too!"""
        pass


@pytest.mark.parametrize(
    "user",
    [
        Goomba(login="admin", password="admin", castle=Castle(name="Lancaster")),
        Goomba(login="megagoomba", password="Qwerty1234", castle=Castle(name="Edinburgh")),
    ],
)
def test_with_user_in_parametrization(user):
    response = requests.post("https://postman-echo.com/post", json=user.dict())
    assert response.json()["data"] == user.dict()
