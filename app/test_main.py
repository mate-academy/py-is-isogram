import pytest
from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("") is True
    assert is_isogram("abiogeneses") is False
    assert is_isogram("cholangiogram") is False
    assert is_isogram("background") is True
    assert is_isogram("alphabet") is False


if __name__ == "__main__":
    pytest.main()
