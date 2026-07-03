from app.main import is_isogram


def test_should_return_true_if_str_empty():
    assert is_isogram("") is True


def test_should_be_case_insensitive():
    assert is_isogram("Adam") is False


def test_should_return_false_when_letters_repeat():
    assert is_isogram("look") is False


def test_should_true_for_isogram():
    assert is_isogram("playground") is True


def test_should_return_non_consecutive_repeating_letters():
    assert is_isogram("alphabet") is False
