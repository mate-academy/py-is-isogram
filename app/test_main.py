from app.main import is_isogram


def test_should_return_true_when_value_have_upper_case_is_isogram():
    assert is_isogram('pLaygrounds') is True


def test_should_return_true_when_value_empty_line_is_isogram():
    assert is_isogram('') is True


def test_non_consecutive_letters_are_not_isogram():
    assert is_isogram('Aa') is False


def test_string_with_different_cases_of_the_same_letter_is_not_isogram():
    assert is_isogram('LdlofokfK') is False