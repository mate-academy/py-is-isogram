from app.main import is_isogram


def test_is_isogram_with_different_cases_of_the_same_letter():
    assert is_isogram("SsSSSsSS") is False


def test_is_isogram_not_only_non_consecutive_not_isogram():
    assert is_isogram("lookdfkl") is False


def test_is_isogram_not_only_consecutive_not_isogram():
    assert is_isogram("look") is False


def test_is_isogram_not_only_consecutive_upper_not_isogram():
    assert is_isogram("LOOK") is False


def test_is_isogram_not_only_consecutive_title_not_isogram():
    assert is_isogram("Look") is False


def test_is_isogram_only_consecutive_title_not_isogram():
    assert is_isogram("Adam'") is False


def test_is_isogram_only_consecutive_is_isogram():
    assert is_isogram("playgrounds") is True


def test_is_isogram_empty_string_is_isogram():
    assert is_isogram("") is True
