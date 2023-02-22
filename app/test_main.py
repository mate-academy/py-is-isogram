from app.main import is_isogram


def test_when_string_is_empty() -> None:
    assert is_isogram("") is True


def test_when_not_isogram_including_capital_letter() -> None:
    assert is_isogram("Adam") is False


def test_when_isogram() -> None:
    assert is_isogram("name") is True


def test_with_ordered_letters() -> None:
    assert is_isogram("zoo") is False