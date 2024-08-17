from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("cat") is True


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_must_be_case_insensitive() -> None:
    assert is_isogram("hello") is False
    assert is_isogram("heLlo") is False


def test_consecutive_repetitions_of_letters_not_isogram() -> None:
    assert is_isogram("doom") is False


def test_non_sequential_repetitions_of_letters_not_isogram() -> None:
    assert is_isogram("dad") is False
