from app.main import is_isogram


def test_words_without_repetitive_letters():
    assert (is_isogram('playgrounds') is True)


def test_words_with_repetitive_letters():
    assert (is_isogram('look') is False)


def test_words_with_big_letters():
    assert (is_isogram('Adam') is False)


def test_empty_line():
    assert (is_isogram('') is True)
