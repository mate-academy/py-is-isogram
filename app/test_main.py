from app.main import is_isogram


def test_isogram_is_case_insensitive():
    assert is_isogram("Adam") is False


# def test_empty_string_is_isogram():
#     assert is_isogram("") is True


def test_non_consecutive_letters_are_not_isogram():
    assert is_isogram()
