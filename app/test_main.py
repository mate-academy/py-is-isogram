from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("")


def test_single_letter() -> None:
    assert is_isogram("a")


def test_same_letter_uppercase_lowercase() -> None:
    assert not is_isogram("Aa")
    assert is_isogram("playgrounds")


def test_non_isogram_due_to_repeated_letter() -> None:
    assert not is_isogram("look")


def test_long_isogram() -> None:
    assert is_isogram("subdermatoglyphic")


def test_word_with_non_letter_characters() -> None:
    assert is_isogram("lumber-jacks")


def test_case_insensitive_isogram() -> None:
    assert is_isogram("DerMatOglYphic")


def test_non_isogram_with_mixed_cases() -> None:
    assert not is_isogram("Alphabet")
