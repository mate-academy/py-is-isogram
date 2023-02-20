from app.main import is_isogram


def test_is_isogram_with_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_with_repeating_one_letter() -> None:
    assert is_isogram("aaa") is False


def test_is_isogram_with_repeating_one_upper_case_letter() -> None:
    assert is_isogram("Aaa") is False


def test_is_isogram_with_repeating_upper_and_lower_case_letter() -> None:
    assert is_isogram("ADad") is False


def test_is_isogram_with_no_repeating_letter() -> None:
    assert is_isogram("Roman") is True
