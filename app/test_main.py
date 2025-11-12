from app.main import is_isogram


def test_true() -> None:
    assert is_isogram("playgrounds") is True


def test_false() -> None:
    assert is_isogram("test") is False


def test_upper_case_false() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True
