import pytest
from .main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds")
    assert is_isogram("abcdefg")
    assert is_isogram("")
    assert is_isogram("Isogram")
    assert is_isogram("Python")

    assert not is_isogram("look")
    assert not is_isogram("Adam")
    assert not is_isogram("hello")
    assert not is_isogram("aabbcc")
    assert not is_isogram("Pythonista")

    if __name__ == "__main__":
        pytest.main()
