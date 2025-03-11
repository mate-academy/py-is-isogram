from app.main import is_isogram


def test_is_isogram_valid_word() -> None:
    assert is_isogram("playgrounds") == True


def test_is_isogram_invalid_word() -> None:
    assert is_isogram("look") == False


def test_is_isogram_invalid_word_case_sensitive() -> None:
    assert is_isogram("Adam") == False


def test_is_isogram_empty_string() -> None:
    assert is_isogram(" ") == True


def test_is_isogram_case_insensitivity() -> None:
    assert is_isogram("Aa") == False
    assert is_isogram("mM") == False
    assert is_isogram("Mm") == False


def test_is_isogram_single_character() -> None:
    assert is_isogram("a") == True
    assert is_isogram("Z") == True


def test_is_isogram_two_same_characters() -> None:
    assert is_isogram("aa") == False
    assert is_isogram("bb") == False
    assert is_isogram("MM") == False


def test_is_isogram_long_word_no_repeat() -> None:
    assert is_isogram("abcdefghijklmno") == True


def test_is_isogram_long_word_with_repeats() -> None:
    assert is_isogram("abcdefghijklmna") == False
    assert is_isogram("abcdefghijklmnaa") == False