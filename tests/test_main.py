from app.main import is_isogram


def test_should_return_true_for_empty_string():
    assert is_isogram("") is True


def test_should_return_true_for_isogram_word_with_big_and_small_letters():
    assert is_isogram("PlayGrounds") is True


def test_should_return_false_for_lowercase_repeating_letters():
    assert is_isogram("opportunity") is False


def test_should_return_false_for_uppercase_repeating_letters():
    assert is_isogram("SUMMER") is False


def test_should_return_false_for_repeating_sensitive_letters():
    assert is_isogram("Test") is False
