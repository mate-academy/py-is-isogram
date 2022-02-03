from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_with_uppercase_letters():
    assert is_isogram("PlaygRound") is True


def test_with_symbls_spaces_and_digits():
    assert is_isogram("abcdefg7. $") is True
