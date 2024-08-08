from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_with_different_letters() -> None:
    assert is_isogram("flower") is True


def test_uppercase_different_letters() -> None:
    assert is_isogram("OSTAP") is True


def test_with_the_same_letter() -> None:
    assert is_isogram("apple") is False


def test_with_uppercase_not_different() -> None:
    assert is_isogram("Alphabet") is False


def test_upper_lower_different() -> None:
    assert is_isogram("Custom") is True
