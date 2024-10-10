from app.main import is_isogram


def test_should_be_case_insensitive() -> None:
    assert is_isogram("plAyGroUnds") is True


def test_should_be_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_be_false_with_different_cases_of_same_letter() -> None:
    assert is_isogram("plAyGraUnds") is False


def test_should_be_false_with_different_cases_of_same_letter_consecutive(

) -> None:
    assert is_isogram("look") is False
