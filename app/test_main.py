from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_with_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_no_register_addicted_letters() -> None:
    assert is_isogram("Adam") is False


def test_non_cosecutive_letters() -> None:
    assert is_isogram("abc") is True


def test_cosecutive_letters() -> None:
    assert is_isogram("look") is False
