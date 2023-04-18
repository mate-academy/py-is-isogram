from app.main import is_isogram


def test_should_return_true() -> None:
    assert is_isogram('playgrounds') == is_isogram('') is True


def test_should_return_false() -> None:
    assert is_isogram('look') == is_isogram('Adam') is False
