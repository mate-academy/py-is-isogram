from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("")


def test_is_isogram_valid_word() -> None:
    assert is_isogram("playgrounds")


def test_is_isogram_invalid_word() -> None:
    assert not is_isogram("look")


def test_is_isogram_invalid_word_case_sensitive() -> None:
    assert not is_isogram("Adam")


def test_is_isogram_case_insensitivity() -> None:
    assert not is_isogram("Aa")
    assert not is_isogram("mM")
    assert not is_isogram("Mm")


def test_is_isogram_single_character() -> None:
    assert is_isogram("a")
    assert is_isogram("Z")


def test_is_isogram_two_same_characters() -> None:
    assert not is_isogram("aa")
    assert not is_isogram("bb")
    assert not is_isogram("MM")


def test_is_isogram_long_word_no_repeat() -> None:
    assert is_isogram("abcdefghijklmno")


def test_is_isogram_long_word_with_repeats() -> None:
    assert not is_isogram("abcdefghijklmna")
    assert not is_isogram("abcdefghijklmnaa")
