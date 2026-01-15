from app.main import is_isogram


def test_empty_string_is_isogram() -> bool:
    assert is_isogram("") is True


def test_isogram_word_is_isogram() -> bool:
    assert is_isogram("playgrounds") is True


def test_non_isogram_word_is_isogram() -> bool:
    assert is_isogram("look") is False


def test_case_insensitivity_is_isogram() -> bool:
    assert is_isogram("Adam") is False
    assert is_isogram("aDam") is False
    assert is_isogram("ADAM") is False


def test_with_punctuation_is_isogram() -> bool:
    assert is_isogram("hello,world!") is False


def test_non_consecutive_letters_are_not_isogram() -> bool:
    assert is_isogram("abcdefghijklmnopqrstuvwxyz") is True
    assert is_isogram("noticeses") is False


def test_consecutive_letters_are_not_isogram() -> bool:
    assert is_isogram("aabbccddeeffgghhii") is False
    assert is_isogram("aaabbbcccddd") is False
