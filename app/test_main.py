from app.main import is_isogram


def test_is_isogram_if_len_word_zero() -> None:
    assert is_isogram("") is True


def test_is_isogram_where_all_letters_dfferent() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_if_have_repetitive_letter_same_register() -> None:
    assert is_isogram("look") is False


def test_is_isogram_if_have_repetitive_letter_different_register() -> None:
    assert is_isogram("Adam") is False
