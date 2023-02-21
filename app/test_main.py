from app.main import is_isogram


def test_with_empty_string_true():
    assert is_isogram("") is True


def test_with_repeating_letter_together_false():
    assert is_isogram("look") is False


def test_with_repeating_letter_not_together_false():
    assert is_isogram("adam") is False


def test_with_different_cases_false():
    assert is_isogram("Adam") is False


def test_with_no_repeating_true():
    assert is_isogram("playgrounds") is True

