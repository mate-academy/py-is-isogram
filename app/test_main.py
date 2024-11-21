from app.main import is_isogram


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("aaBbcc") is False
    assert is_isogram("abac") is False
    assert is_isogram("Abcdef") is True
    assert is_isogram("") is True
