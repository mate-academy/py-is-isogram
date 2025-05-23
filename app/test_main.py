from app.main import is_isogram


def test_isogram_false_case_insensitive() -> None:
    assert is_isogram("Adam") is False, \
        "Function should be case-insensitive"


def test_isogram_true_empty_string() -> None:
    assert (is_isogram("") is True), \
        "Empty string is an isogram"


def test_isogram_false_consecutive_letters() -> None:
    assert (is_isogram("apple") is False), \
        "String have consecutive letters, it`s not isogram"
