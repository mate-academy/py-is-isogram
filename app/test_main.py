from app.main import is_isogram


def test_empty_string():
    assert is_isogram('') is True


def test_should_be_case_insensitive():
    assert is_isogram('Adam') is False


def test_should_be_has_no_repeating_latters():
    assert is_isogram('look') is False
