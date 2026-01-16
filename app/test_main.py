from app.main import is_isogram


def test_of_different_cases_of_the_same_letter() -> None:
    assert is_isogram("Adam") is False


def test_of_empty_string_as_an_isogram() -> None:
    assert is_isogram("") is True


def test_only_consecutive_letters() -> None:
    assert is_isogram("look") is False


def test_only_non_consecutive_letters() -> None:
    assert is_isogram("playgrounds") is True
