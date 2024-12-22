import pytest
from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram('playgrounds') is True, "Test case 'playgrounds' failed"
    assert is_isogram('look') is False, "Test case 'look' failed"
    assert is_isogram('Adam') is False, "Test case 'Adam' failed"
    assert is_isogram('') is True, "Test case empty string failed"
    assert is_isogram('Dermatoglyphics') is True, "Test case 'Dermatoglyphics' failed"
    assert is_isogram('aba') is False, "Test case 'aba' failed"
    assert is_isogram('moOse') is False, "Test case 'moOse' failed"
    assert is_isogram('abcdefg') is True, "Test case 'abcdefg' failed"
    assert is_isogram('isogram') is True, "Test case 'isogram' failed"
    assert is_isogram('repeated') is False, "Test case 'repeated' failed"


if __name__ == "__main__":
    pytest.main()
