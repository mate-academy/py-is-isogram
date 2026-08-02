from app.main import is_isogram


def test_have_any_different_between_register_repeating_letters() -> None:
    assert is_isogram("Adam") is False


def test_have_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_dont_have_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_have_empty_string() -> None:
    assert is_isogram("") is True
