from app.main import is_isogram


def test_isogram_without_repetitions() -> None:
    assert is_isogram("playgrounds") is True


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("Deepl") is False


def test_isogram_case_insensitive() -> None:
    assert is_isogram("Examples") is False


def test_empty_string_isogram() -> None:
    assert is_isogram("") is True
