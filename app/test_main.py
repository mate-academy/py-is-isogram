from app.main import is_isogram


def test_empty_string_is_isogram():
    word = ""
    assert is_isogram(word)


def test_isogram_is_case_insensitive():
    word = "Adam"
    assert not is_isogram(word)


def test_consecutive_letters_are_not_isogram():
    word = "look"
    assert not is_isogram(word)


def test_non_consecutive_letters_are_not_isogram():
    word = "asa"
    assert not is_isogram(word)
