from app.main import is_isogram


def test_empty_word():
    assert (is_isogram('') == True)


def test_word_with_chars_not_repeat():
    assert (is_isogram('playgrounds') is True)


def test_word_with_chars_repeated():
    assert (is_isogram('look') is False)


def test_word_with_different_char_register():
    assert (is_isogram('Adam') is False)
