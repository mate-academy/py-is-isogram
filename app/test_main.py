from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_playground_is_isogram() -> None:
    assert (is_isogram("playground") is True)


def test_word_with_lower_case_duplicates_is_isogram() -> None:
    assert (is_isogram("look") is False)


def test_word_with_upper_case_duplicates_is_isogram() -> None:
    assert (is_isogram("oleksII") is False)


def test_word_with_upper__and_lower_case_duplicates_is_isogram() -> None:
    assert (is_isogram("aNton") is False)


def test_word_with_hyphens_is_isogram() -> None:
    assert (is_isogram("abc-def-ghi") is False)
