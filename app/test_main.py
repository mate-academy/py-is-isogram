from app.main import is_isogram


def test_should_detect_regular_words() -> None:
    assert is_isogram("regular") is False


def test_should_return_true_when_word_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_should_be_case_insensitive() -> None:
    assert is_isogram("JaCk") is True


def test_different_cases_of_same_letter_is_not_isogram() -> None:
    assert is_isogram("Ggt") is False
