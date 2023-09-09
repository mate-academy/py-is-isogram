from app.main import is_isogram


def test_lower_and_upper_case_characters():
    assert is_isogram("Ana") is False


def test_duplicated_characters():
    assert is_isogram("Anaana") is False


def test_should_return_true_for_empty_string():
    assert is_isogram("") is True


def test_should_return_true_for_isogram():
    assert is_isogram("Ane") is True


def test_for_non_letter_characters():
    assert is_isogram("An00") is False


