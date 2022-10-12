from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_string_diff_case():
    assert is_isogram("look") is False


def test_big_letters():
    assert is_isogram("Adam") is False
