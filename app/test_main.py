from app.main import is_isogram


def test_empty_string():
    assert is_isogram("") is True


def test_return_expected_result_when_word_isogram():
    assert is_isogram("playgrounds") is True


def test_return_expected_result_when_word_not_isogram():
    assert is_isogram("look") is False


def test_check_case():
    assert is_isogram("Adam") is False
