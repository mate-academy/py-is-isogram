from app import main


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("")


def test_isogram_word_returns_true() -> None:
    assert main.is_isogram("playgrounds")


def test_case_insensitive_repeating_letter_returns_false() -> None:
    assert not main.is_isogram("Adam")


def test_consecutive_repeating_letters_return_false() -> None:
    assert not main.is_isogram("look")


def test_non_consecutive_repeating_letters_return_false() -> None:
    assert not main.is_isogram("bananas")
