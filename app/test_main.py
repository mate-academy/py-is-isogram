from app.main import is_isogram


def test_return_true_only_letters():
    assert is_isogram('playgrounds') is True


def test_return_false_when_letter_repeats():
    assert is_isogram('look') is False


def test_return_false_when_letter_repeats_lower_upper():
    assert is_isogram('Adam') is False


def test_return_true_when_empty():
    assert is_isogram('') is True
