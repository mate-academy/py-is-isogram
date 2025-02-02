from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_playgrounds() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_look() -> None:
    assert is_isogram("look") is False


def test_is_isogram_adam_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_single_letter() -> None:
    assert is_isogram("a") is True


def test_is_isogram_mixed_case() -> None:
    assert is_isogram("AbZ") is True


def test_is_isogram_repeated_mixed_case() -> None:
    assert is_isogram("aAbB") is False


def test_is_isogram_long_non_isogram() -> None:
    assert is_isogram("abcdefghijkalm") is False
