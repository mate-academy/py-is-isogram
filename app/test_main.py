from app.main import is_isogram


def test_should_return_true_when_value_isogram():
    assert is_isogram('pLaygrounds') is True


def test_return_true_value_empty_line_isogram():
    assert is_isogram('') is True


def test_non_consecutive_letters_are_not_isogram():
    assert is_isogram('Aa') is False


def test_different_cases_same_letter_not_isogram():
    assert is_isogram('LdlofokfK') is False
