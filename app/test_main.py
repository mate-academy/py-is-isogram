from app.main import is_isogram


def test_get_True_if_not_the_same_latters():
    assert is_isogram('playgrounds') is True


def test_get_False_if_word_have_the_same_latters():
    assert is_isogram('look') is False


def test_get_False_if_word_have_the_same_upper_latter():
    assert is_isogram('Adam') is False


def test_get_True_if_empty_string():
    assert is_isogram('') is True
