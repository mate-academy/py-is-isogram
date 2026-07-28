from app.main import is_isogram


def test_isogram_returns_true_for_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_isogram_returns_false_for_consecutive_duplicates() -> None:
    assert is_isogram("look") is False


def test_isogram_returns_false_for_non_consecutive_duplicates() -> None:
    assert is_isogram("alphabet") is False


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True
