from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_false_with_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_all_unique_case_insensitive() -> None:
    assert is_isogram("AbcDefG")
