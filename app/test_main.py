from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_case_insensitivity():
    assert is_isogram("AaBb") is False


def test_nonconsecutive_word():
    assert is_isogram("Adam") is False


def test_function_is_true():
    assert is_isogram("playgrounds") is True
