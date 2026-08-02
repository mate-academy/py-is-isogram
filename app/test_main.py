from app.main import is_isogram


def test_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_isogram_false_with_repeats() -> None:
    assert is_isogram("look") is False


def test_isogram_false_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_single_letter() -> None:
    assert is_isogram("A") is True


def test_isogram_long_valid_word() -> None:
    assert is_isogram("background") is True


def test_isogram_with_multiple_repeats() -> None:
    assert is_isogram("banana") is False


def test_isogram_all_unique_letters() -> None:
    assert is_isogram("subdermatoglyphic") is True
