from app.main import is_isogram


def test_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False, \
        "The word 'Adam' should not be an isogram"
    assert is_isogram("adam") is False, \
        "The word 'adam' should not be an isogram"
    assert is_isogram("A") is True, \
        "The word 'A' should be an isogram"


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True, \
        "The empty string should be considered an isogram"


def test_non_consecutive_letters_are_isogram() -> None:
    assert is_isogram("playgrounds") is True, \
        "The word 'playgrounds' should be an isogram"
    assert is_isogram("look") is False, \
        "The word 'look' should not be an isogram"


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("aab") is False, \
        "The word 'aab' should not be an isogram"
    assert is_isogram("ab") is True, \
        "The word 'ab' should be an isogram"
