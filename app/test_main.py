from app.main import is_isogram


def test_should_be_empty_string():
    assert is_isogram("") is True


def test_should_be_uppercase():
    assert is_isogram("PLAYGROUNDS") is True


def test_without_consecutive():
    assert is_isogram("look") is False


def test_should_be_lowercase():
    assert is_isogram("playgrounds") is True


def test_without_different_cases():
    assert is_isogram("Adam") is False
