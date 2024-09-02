from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("")


def test_case_sensitive() -> None:
    assert is_isogram("Dermatoglyphics")


def test_non_isogram() -> None:
    assert not is_isogram("Adam")


def test_string_with_spaces() -> None:
    assert not is_isogram("hello world")


def test_string_with_special_characters() -> None:
    assert is_isogram("!@#&*")


def test_string_with_numbers() -> None:
    assert is_isogram("1234567890")
