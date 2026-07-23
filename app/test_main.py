from app.main import is_isogram


def test_is_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_false() -> None:
    assert is_isogram("fool") is False


def test_same_registr_letters() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True
