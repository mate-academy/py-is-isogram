import pytest
from app.main import is_isogram


@pytest.mark.parametrize("name", ["playgrounds", " ", "abc"])
def test_positive_isogram(name: str) -> None:
    assert is_isogram(name)


@pytest.mark.parametrize("name", ["look", "Adam"])
def test_negative_isogram(name: str) -> None:
    assert not is_isogram(name)


@pytest.mark.parametrize("name", [True, 123, {"key": 25}])
def test_incorrect_value(name: str) -> None:
    with pytest.raises(ValueError):
        is_isogram(name)
