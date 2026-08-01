from app.main import is_isogram


# write your code here
def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_valid_isogram_lowercase() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_case_insensitive_repetition() -> None:
    assert is_isogram("Adam") is False


def test_all_unique_letters_mixed_case() -> None:
    assert is_isogram("Machine") is True


def test_repeated_letters_mixed_case() -> None:
    assert is_isogram("Programming") is False
