from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_different_case_of_the_same_letter():
    assert is_isogram("Adam") is False


def test_non_consecutive_letters():
    assert is_isogram("playground") is True


def test_string_gives_true():
    assert is_isogram("generation") is False
