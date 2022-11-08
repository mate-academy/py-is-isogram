from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_one_letter() -> None:
    assert is_isogram("a") is True


def test_consistent_letters() -> None:
    assert is_isogram("look") is False


def test_non_consistent_letters() -> None:
    assert is_isogram("loko") is False


def test_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_case_insensitity() -> None:
    assert is_isogram("Adam") is False
