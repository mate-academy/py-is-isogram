from app.main import is_isogram


def test_should_return_true_if_word_has_no_repeating_letters():
    assert is_isogram('playgrounds') is True


def test_should_return_false_if_word_has_repeating_letters():
    assert is_isogram('look') is False


def test_should_check_that_function_is_case_insensitive():
    assert is_isogram('Adam') is False


def test_should_return_true_if_word_is_empty():
    assert is_isogram('') is True
