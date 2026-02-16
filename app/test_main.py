from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_word_without_repeats() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeats() -> None:
    assert is_isogram("look") is False


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("aA") is False


def test_single_character() -> None:
    assert is_isogram("x") is True


def test_long_word_with_repeat() -> None:
    assert is_isogram("Alphabet") is False


def test_long_word_without_repeat() -> None:
    assert is_isogram("Subdermatoglyphic") is True
