from app.main import is_isogram


def test_long_word_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_short_word_non_isogram() -> None:
    assert is_isogram("oo") is False


def test_big_and_small_letter_equal() -> None:
    assert is_isogram("Adam") is False


def test_string_empty() -> None:
    assert is_isogram("") is True
