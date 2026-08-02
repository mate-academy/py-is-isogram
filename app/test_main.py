from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_isogram_with_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_non_isogram_with_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_non_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_isogram_with_mixed_case() -> None:
    assert is_isogram("PyThOn") is True


def test_isogram_with_single_letter() -> None:
    assert is_isogram("a") is True


def test_isogram_with_repeating_letter() -> None:
    assert is_isogram("apple") is False
