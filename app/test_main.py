from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_single_letter() -> None:
    assert is_isogram("A") is True


def test_all_unique_lowercase() -> None:
    assert is_isogram("playgrounds") is True


def test_repeated_letters_consecutive() -> None:
    assert is_isogram("look") is False


def test_repeated_letters_non_consecutive() -> None:
    assert is_isogram("banana") is False


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("Machine") is True
    assert is_isogram("UnIqUe") is False


def test_all_unique_mixed_case() -> None:
    assert is_isogram("Python") is True


def test_long_isogram() -> None:
    word = "Dermatoglyphics"  # known longest English isogram
    assert is_isogram(word) is True
