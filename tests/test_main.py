from app.main import is_isogram


def test_empty_string():
    assert is_isogram('')


def test_repeated_sensitive_letters():
    assert not is_isogram('Adam')


def test_string_without_repeating():
    assert is_isogram('playgrounds')


def test_letters_repeat():
    assert not is_isogram("ObhhjkoOpbB")
