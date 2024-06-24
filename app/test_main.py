import pytest
from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("") is True
    assert is_isogram("abiogeneses") is False
    assert is_isogram("cholangiogram") is False
    assert is_isogram("background") is True
    assert is_isogram("alphabet") is False


def test_edge_cases() -> None:
    assert is_isogram("Aa") is False
    assert is_isogram("AaAaAa") is False
    assert is_isogram("abcdefgh") is True
    assert is_isogram("abcdefgha") is False
    assert is_isogram("a") is True


if __name__ == "__main__":
    pytest.main()
