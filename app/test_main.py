from app.main import is_isogram


def test_word_string_is_empty() -> None:
    assert is_isogram("") is True


def test_word_without_repeated_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_with_same_letters_in_different_registers() -> None:
    assert is_isogram("Adam") is False
