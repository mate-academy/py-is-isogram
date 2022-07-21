from app.main import is_isogram


def test_empty_string_is_isogram():
    word = ""
    assert is_isogram(word)


def test_isogram_is_case_insensitive():
    word = "Member"
    assert not is_isogram(word)


def test_consecutive_letters_are_not_isogram():
    word = "Book"
    assert not is_isogram(word)


def test_non_consecutive_letters_are_not_isogram():
    word = "playgrounds"
    assert not is_isogram(word)
