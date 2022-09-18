from app.main import is_isogram


def test_should_return_true_when_word_is_empty_string():
    assert is_isogram("") is True


def test_should_return_false_when_word_has_repeating_letters():
    assert is_isogram("fool") is False


def test_should_return_false_if_word_has_repeating_case_varied_letters():
    assert is_isogram("Adam") is False


def test_should_return_true_when_word_has_no_repeating_letters():
    assert is_isogram("playgrounds") is True
