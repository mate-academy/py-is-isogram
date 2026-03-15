import pytest
from app import main


@pytest.mark.parametrize("word", ["Label", "carpenter", "Simplisity"])
def test_is_isogram(word: str) -> None:
    assert main.is_isogram(word) is False


def test_is_empty_string() -> None:
    assert main.is_isogram("") is True
