from app.main import is_isogram


def test_empty():
    assert is_isogram("") is True


def test_true():
    assert is_isogram("playgrounds") is True


def test_false():
    assert is_isogram("look") is False


def test_case_insensitive():
    assert is_isogram("Adam") is False
