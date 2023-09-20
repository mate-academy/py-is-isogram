from app.main import is_isogram


def test_no_repeat_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_repeat_letters() -> None:
    assert is_isogram("look") is False


def test_no_repeat_but_recur() -> None:
    assert is_isogram("Adam") is False


def test_string_is_empty() -> None:
    assert is_isogram("") is True
