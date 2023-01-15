from app.main import is_isogram


def test_empty_string() -> None:
    assert (is_isogram(""))


def test_small_large_later() -> None:
    assert (is_isogram("Adam") is False)


def test_iso_on_false() -> None:
    assert (is_isogram("look") is False)


def test_iso_on_true() -> None:
    assert (is_isogram("ozark") is True)
