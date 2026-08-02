from app.main import is_isogram


def test_name_is_false() -> None:
    assert is_isogram("Adam") is False


def test_symbol_how_non_consecutive() -> None:
    assert is_isogram("playgrounds") is True


def test_symbol_how_consecutive() -> None:
    assert is_isogram("look") is False


def test_return_true_if_zero_symbal() -> None:
    assert is_isogram("") is True
