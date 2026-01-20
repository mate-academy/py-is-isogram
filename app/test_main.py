from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_non_empty_string() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_the_capital_letter() -> None:
    assert is_isogram("Adam") is False
