from app.main import is_isogram


def test_common() -> None:
    assert is_isogram("playgrounds") is True


def test_double_letter() -> None:
    assert is_isogram("look") is False


def test_double_letter_different_case() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_single_letter() -> None:
    assert is_isogram("a") is True


def test_upper_case() -> None:
    assert is_isogram("ABCFD") is True


def test_only_single_letter() -> None:
    assert is_isogram("aaaaa") is False
