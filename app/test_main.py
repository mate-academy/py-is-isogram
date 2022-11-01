from app.main import is_isogram


def test_return_true_for_upper_and_lower_case() -> None:
    assert is_isogram("PlayGrOundS") is True


def test_null_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_different_cases_the_same_letter_is_no_isogram() -> None:
    assert is_isogram("aSsert") is False


def test_two_same_letters_is_no_isogram() -> None:
    assert is_isogram("look") is False


def test_two_same_non_consecutive_letters_is_no_isogram() -> None:
    assert is_isogram("marathon") is False
