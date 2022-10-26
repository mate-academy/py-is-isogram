from app.main import is_isogram


def test_return_true_when_word_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_return_true_when_word_is_empty() -> None:
    assert is_isogram("") is True


def test_return_false_when_letter_repeated() -> None:
    assert is_isogram("look") is False


def test_return_false_when_letter_case_insensitive() -> None:
    assert is_isogram("Adam") is False
