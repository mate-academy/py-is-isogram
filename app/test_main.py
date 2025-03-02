from app.main import is_isogram  # Assuming the function is inside app/main.py


def test_empty_string() -> None:
    assert is_isogram("")


def test_isogram_lowercase() -> None:
    assert is_isogram("playgrounds")


def test_non_isogram_repeating_letters() -> None:
    assert not is_isogram("look")


def test_case_insensitive() -> None:
    assert not is_isogram("Adam")


def test_isogram_mixed_case() -> None:
    assert is_isogram("BlueSky")


def test_isogram_with_long_unique_letters() -> None:
    assert is_isogram("subdermatoglyphic")


def test_non_isogram_with_spaces() -> None:
    assert not is_isogram("hello world")
    # Spaces should be ignored but 'l' repeats


def test_non_isogram_mixed_case() -> None:
    assert not is_isogram("Alphabet")


def test_isogram_single_letter() -> None:
    assert is_isogram("A")


def test_isogram_repeating_letters_non_consecutive() -> None:
    assert not is_isogram("banana")
