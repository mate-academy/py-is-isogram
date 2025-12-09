from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_with_repeats() -> None:
    assert is_isogram("look") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("Python") is True


def test_is_isogram_single_letter() -> None:
    assert is_isogram("A") is True


def test_is_isogram_with_non_letter_chars() -> None:
    result: bool = is_isogram("a-b-c")
    assert isinstance(result, bool)
