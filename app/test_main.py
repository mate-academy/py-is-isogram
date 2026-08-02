from app.main import is_isogram


def test_with_empty_string() -> None:
    assert is_isogram("") is True


def test_if_program_is_case_consecutive() -> None:
    word = "Adam"
    assert is_isogram(word) is False


def test_with_duplicates() -> None:
    assert is_isogram("look") is False


def test_with_only_upper_letters() -> None:
    assert is_isogram("ABCVSDA") is False
