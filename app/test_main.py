from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_up_down() -> None:
    assert is_isogram("Adam") is False


def test_different_letters() -> None:
    assert is_isogram("playground") is True


def test_is_in_a_row() -> None:
    assert is_isogram("abba") is False
