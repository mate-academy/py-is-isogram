from app.main import is_isogram  # adjust import path as needed


def test_isogram_with_normal_word() -> None:
    assert is_isogram("playgrounds")


def test_isogram_with_repeating_letters() -> None:
    assert not is_isogram("look")


def test_isogram_case_insensitive() -> None:
    assert not is_isogram("Adam")


def test_isogram_with_empty_string() -> None:
    assert is_isogram("")


def test_isogram_single_letter() -> None:
    assert is_isogram("x")


def test_isogram_long_word() -> None:
    # A long known isogram
    assert is_isogram("subdermatoglyphic")


def test_isogram_long_non_isogram() -> None:
    # Has repeating 'c', 'a', 'r', 'l'
    assert not is_isogram("characteristically")
