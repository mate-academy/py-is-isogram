from app.main import is_isogram


def test_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_isogram_false_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_isogram_false_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_all_unique_uppercase() -> None:
    assert is_isogram("PYTHON") is True


def test_isogram_all_unique_mixed_case() -> None:
    assert is_isogram("Python") is True


def test_isogram_single_letter() -> None:
    assert is_isogram("a") is True


def test_isogram_two_same_letters_different_case() -> None:
    assert is_isogram("Aa") is False
