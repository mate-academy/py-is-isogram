from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_repeating_letters() -> None:
    assert is_isogram("Adam") is False


def test_repeating_lower_letters() -> None:
    assert is_isogram("look") is False


def test_single_letter() -> None:
    assert is_isogram("A") is True
