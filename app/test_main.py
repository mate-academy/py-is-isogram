import pytest
from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("") is True
    assert is_isogram("abcdef") is True
    assert is_isogram("AaBbCc") is False
    assert is_isogram("unique") is False
    assert is_isogram("repeated") is False
    assert is_isogram("hello") is False
    assert is_isogram("world") is True


if __name__ == "__main__":
    pytest.main()
