from app.main import is_isogram


def test_when_word_is_empty() -> None:
    assert is_isogram("") is True


def test_when_word_count_letter_more_than_one() -> None:
    assert is_isogram("look") is False


def test_when_word_count_letter_is_one() -> None:
    assert is_isogram("playgrounds") is True


def test_when_there_are_different_case_letters_in_a_word() -> None:
    assert is_isogram("Adam") is False
