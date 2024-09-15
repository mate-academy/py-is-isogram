from app.main import is_isogram


def test_should_return_true_if_string_empty():
    assert is_isogram('') is True


def test_if_program_is_test_insensitive():
    assert is_isogram('Adam') is False


def test_short_word():
    assert is_isogram('look') is False


def test_long_word():
    assert is_isogram('playgrounds') is True
