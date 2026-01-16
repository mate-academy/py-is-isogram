from app.main import is_isogram


def test_return_true_when_empty_string():
    assert is_isogram("") is True


def test_case_insensitive():
    assert is_isogram("Sos") is False


def test_return_true_when_no_repeating_letters():
    assert is_isogram("cyberpunk") is True


def test_return_false_when_word_has_repeating_letters():
    assert is_isogram("book") is False
