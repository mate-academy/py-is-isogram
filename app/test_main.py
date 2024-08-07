from app.main import is_isogram


def test_empty_string_returns_true() -> None:
    assert is_isogram("") is True


def test_correct_word_returns_true() -> None:
    assert is_isogram("playgrounds") is True


def test_incorrect_word_returns_true() -> None:
    assert is_isogram("look") is False


def test_word_is_capitalized_but_it_is_repeated() -> None:
    assert is_isogram("Adam") is False
