from app.main import is_isogram


def test_if_string_is_empty() -> None:
    assert is_isogram("") is True


def test_if_string_has_the_same_consecutive_letters() -> None:
    assert is_isogram("look") is False


def test_if_string_has_same_non_consecutive_and_capital_letters() -> None:
    assert is_isogram("Adam") is False


def test_if_string_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
