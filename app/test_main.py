from app.main import is_isogram


def test_check_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_check_duplicates() -> None:
    assert is_isogram("look") is False


def test_check_capital_letters() -> None:
    assert is_isogram("Adam") is False


def test_check_empty_value() -> None:
    assert is_isogram("") is True
