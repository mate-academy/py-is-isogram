from app.main import is_isogram

def test_if_empty_string_is_isogram() -> None:
    word = ""
    assert is_isogram(word), "The empty string is an isogram"


def test_if_duplicate_is_isogram() -> None:
    word = "look"
    assert is_isogram(word), "Duplicate letters cannot be in an isogram"


def test_if_upper_and_lower_case_included() -> None:
    word = "Adam"
    assert is_isogram(word), "Upper and lower case are not included"


def test_if_string_type() -> None:
    word = 532
    assert is_isogram(word), "Isogram has a string type"
