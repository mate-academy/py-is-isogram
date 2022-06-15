from app.main import is_isogram


def test_empty_string():
    given_word = is_isogram("")
    assert given_word is True


def test_long_word_without_duplicates_of_letters():
    given_word = is_isogram("playgrounds")
    assert given_word is True


def test_short_word_with_double_o():
    given_word = is_isogram("look")
    assert given_word is False


def test_short_word_with_uppercase_and_lowercase():
    given_word = is_isogram("Adam")
    assert given_word is False
