from app.main import is_isogram


def test_empty_word() -> None:
    assert (is_isogram("") is True)


def test_big_small_letter() -> None:
    assert (is_isogram("Adam") is False)


def test_double_letters() -> None:
    assert (is_isogram("look") is False)


def test_long_word() -> None:
    assert (is_isogram("playgrounds") is True)
