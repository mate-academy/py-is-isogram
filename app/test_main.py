from app.main import is_isogram


def test_should_return_true_when_string_empty():
    assert is_isogram('') is True


def test_should_return_true_when_string_have_no_repeat_letter():
    assert is_isogram('playgrounds') is True


def test_should_return_false_when_string_have_two_and_more_same_letter_and_different_case():
    assert is_isogram('Adam') is False


def test_should_return_false_when_string_have_two_and_more_same_letter():
    assert is_isogram('look') is False
