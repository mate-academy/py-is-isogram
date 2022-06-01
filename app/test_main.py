from app.main import is_isogram


def test_is_isogram_empty_string():
    assert is_isogram('') is True


def test_is_isogram_case():
    assert is_isogram('Adam') is False


def test_is_isogram_repeat():
    assert is_isogram('intelligence') is False


def test_is_isogram_no_repeats():
    assert is_isogram('globe') is True
