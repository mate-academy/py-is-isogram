from app.main import is_isogram


def test_function_returns_bool() -> None:
    assert isinstance(is_isogram(""), bool)


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_uppercase_words() -> None:
    assert is_isogram("HeLlo") is False


def test_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_non_consecutive_repeating_letters() -> None:
    assert is_isogram("Taras") is False


def test_non_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True
