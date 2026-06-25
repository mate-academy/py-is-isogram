from app.main import is_isogram

def test_empty_string() -> bool:
    assert is_isogram('') is True

def test_word_with_unique_letters() -> bool:
    assert is_isogram('abcd') is True

def test_word_with_repeated_letters() -> bool:
    assert is_isogram("aba") is False


def test_case_insensitive() -> bool:
    assert is_isogram("Aa") is False
