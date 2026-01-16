from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_words() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("uncopyrightable") is True
    assert is_isogram("Houseplant") is True


def test_non_isogram_words() -> None:
    assert is_isogram("look") is False
    assert is_isogram("banana") is False
    assert is_isogram("Mississippi") is False


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("Dermatoglyphics") is True
