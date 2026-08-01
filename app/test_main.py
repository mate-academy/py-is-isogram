from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_repetition_of_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_repetition_of_letters_with_different_cases() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_the_empty_string() -> None:
    assert is_isogram("") is True
