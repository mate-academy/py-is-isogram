from app.main import is_isogram


def test_word_is_empty() -> None:
    assert is_isogram("")


def test_word_which_is_not_isogram() -> None:
    assert is_isogram("Joe")


def test_word_which_is_isogram() -> None:
    assert not is_isogram("Apple")


def test_is_case_insensitive() -> None:
    assert not is_isogram("Adam")
