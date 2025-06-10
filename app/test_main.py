from app.main import is_isogram


def test_first() -> None:
    assert is_isogram('playgrounds') is True


def test_second() -> None:
    assert is_isogram('look') is False


def test_third() -> None:
    assert is_isogram('Adam') is False


def test_fourth() -> None:
    assert is_isogram('') is True
