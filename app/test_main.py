from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_repeated():
    assert is_isogram('look') is False


def test_apper_case():
    assert is_isogram('Adam') is False


def test_all():
    assert is_isogram('playgrounds') is True
