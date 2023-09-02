import pytest
from pydantic.v1 import BaseModel


class User(BaseModel):
    login: str
    password: str

    def sign_in(self):
        ...


@pytest.fixture
def signed_in_user(request):
    login = request.param.get("login")
    password = request.param.get("password")
    return User(login=login, password=password).sign_in()


@pytest.mark.parametrize(
    "signed_in_user", [{"login": "login@mailserver.com", "password": "test_password"}], indirect=True
)
def test_indirect(signed_in_user):
    ...
