from app.main import is_isogram


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("aabbcc") == False
    assert is_isogram("abac") == False
    assert is_isogram("abcdef") == True
