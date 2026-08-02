from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_non_empty_string() -> None:
    assert is_isogram("playgrounds") is True


def test_different_cases_of_the_same_letter() -> None:
    assert is_isogram("Adam") is False


def test_different_cases_of_the_same_consecutive_letter() -> None:
    assert is_isogram("MoOd") is False


def test_same_cases_of_the_same_consecutive_letter() -> None:
    assert is_isogram("look") is False
