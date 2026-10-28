from app import main


def test_isogram_with_unique_letters() -> None:
    assert main.is_isogram("playgrounds") is True


def test_word_with_repeated_letters() -> None:
    assert main.is_isogram("look") is False


def test_repeated_letters_with_different_cases() -> None:
    assert main.is_isogram("Adam") is False


def test_empty_string() -> None:
    assert main.is_isogram("") is True


def test_isogram_with_uppercase_letters() -> None:
    assert main.is_isogram("Python") is True


def test_repeated_letters_not_next_to_each_other() -> None:
    assert main.is_isogram("elephant") is False


def test_all_letters_are_unique() -> None:
    assert main.is_isogram("lamp") is True


def test_same_letter_in_different_cases() -> None:
    assert main.is_isogram("mM") is False
