import pytest
from app.main import is_isogram


@pytest.mark.parametrize("text", ["", "playgrounds", "a"])
def test_isogram_true(text: str) -> None:
    assert is_isogram(text)


@pytest.mark.parametrize("text", ["look", "Adam", "aA", "local"])
def test_isogram_false(text: str) -> None:
    assert not is_isogram(text)
