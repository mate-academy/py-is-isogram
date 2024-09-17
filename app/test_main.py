from app.main import is_isogram


def test_if_string_is_empty():
    assert is_isogram("") is True


def test_when_string_have_different_size_letters():
    assert is_isogram("EmPTy") is True


def test_when_str_include_same_title_letters():
    assert is_isogram("FFFFFFFFF") is False


def test_when_str_include_one_letter_in_diff_cases():
    assert is_isogram("Ff") is False


def test_random_big_str():
    assert is_isogram("Documentation") is False
