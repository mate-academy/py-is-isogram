from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_is_isogram_returns_true_for_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_returns_false_for_non_isogram() -> None:
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Mama") is False
    assert is_isogram("mama") is False


def test_is_isogram_with_repeating_characters() -> None:
    assert is_isogram("hello") is False
    assert is_isogram("world") is True
