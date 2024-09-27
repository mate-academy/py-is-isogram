from app.main import is_isogram


def test_should_return_true_if_word_equal_empty():
    assert is_isogram("") is True


def test_should_be_case_insensitive():
    assert is_isogram("Adam") is False


def test_has_repeating_letters_consecutive():
    assert is_isogram("look") is False


def test_has_no_repeating_letters():
    assert is_isogram("playground") is True
