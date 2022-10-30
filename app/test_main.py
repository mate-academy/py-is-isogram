from app.main import is_isogram


def test_should_retern_true_when_input_is_empty_string() -> None:
    assert is_isogram("") is True


def test_should_retern_true_when_input_is_isogram() -> None:
    assert is_isogram("qwerty") is True


def test_should_retern_false_when_input_is_not_isogram() -> None:
    assert is_isogram("abba") is False


def test_return_false_when_letter_case_insensitive() -> None:
    assert is_isogram("Adam") is False
