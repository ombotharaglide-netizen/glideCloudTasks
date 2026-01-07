import pytest
from pydantic import ValidationError
from models import User


def test_user_model_valid():
    u = User(name="Sam", email="s@example.com", age=40)
    assert u.name == "Sam"


def test_user_model_invalid_age():
    with pytest.raises(ValidationError):
        User(name="Sam", email="s@example.com", age="forty")
