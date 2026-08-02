from app.main import is_isogram


def test_right_word() -> None:
    test_word = "playground"
    assert is_isogram(test_word) is True


def test_not_isogram() -> None:
    test_word = "look"
    assert is_isogram(test_word) is False


def test_isogram_is_case_insensitive() -> None:
    test_word = "Adam"
    assert is_isogram(test_word) is False


def test_empty_string_is_isogram() -> None:
    test_word = ""
    assert is_isogram(test_word) is True
