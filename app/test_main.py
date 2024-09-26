from app.main import is_isogram


def test_empty_string_is_isogram():
    assert is_isogram("") is True


def test_isogram_is_case_insensitive():
    assert is_isogram("Aavt") is False


def test_consecutive_letters_are_not_isogram():
    assert is_isogram("sdeegq") is False


def test_non_consecutive_letters_are_not_isogram():
    assert is_isogram("AfBqrtf") is False
