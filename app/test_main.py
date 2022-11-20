from app.main import is_isogram


def test_should_return_bool() -> None:
    assert isinstance(is_isogram("abc"), bool) is True


def test_empty_str() -> None:
    assert is_isogram("") is True


def test_str_should_return_true() -> None:
    assert is_isogram("playgrounds") is True


def test_str_should_return_false() -> None:
    assert is_isogram("look") is False


def test_case_sensitive_should_return_false() -> None:
    assert is_isogram("Adam") is False
