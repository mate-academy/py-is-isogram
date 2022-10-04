from app.main import is_isogram


def test_should_return_expected_result_when_word_is_isogram():
    assert is_isogram('playgrounds') is True


def test_should_return_expected_result_when_word_isnt_isogram():
    assert is_isogram('look') is False


def test_should_check_case_insensitivity_of_function():
    assert is_isogram('Adam') is False


def test_should_return_true_when_word_is_empty():
    assert is_isogram('') is True
