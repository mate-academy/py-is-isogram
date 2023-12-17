from app.main import is_isogram


def test_when_func_takes_empty_string():
    assert is_isogram("") is True


def test_when_func_takes_unique_letters_in_string():
    assert is_isogram("abcd") is True


def test_when_func_takes_the_same_letters():
    assert is_isogram("mama") is False


def test_when_func_takes_upper_and_lower_the_same_letters():
    assert is_isogram("Oslo") is False
