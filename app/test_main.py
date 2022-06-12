from app.main import is_isogram


def test_isogram_when_no_repeating_letters():
    assert is_isogram('playgrounds') is True


def test_isogram_when_empty_string():
    assert is_isogram('') is True


def test_function_should_be_case_insensitive():
    assert is_isogram('Adam') is False


def test_not_isogram_when_repeating_consecutive_letters():
    assert is_isogram('look') is False


def test_not_isogram_when_repeating_non_consecutive_letters():
    assert is_isogram('tomato') is False
