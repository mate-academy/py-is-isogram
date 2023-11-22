from app.main import is_isogram


def test_returns_true_with_empty_string() -> None:
    assert is_isogram("") is True


def test_different_cases_considered_as_same_letter() -> None:
    assert is_isogram("Adam") is False


def test_negative_same_upper_case_letters() -> None:
    assert is_isogram("lOOk") is False


def test_negative_same_lower_case_letters() -> None:
    assert is_isogram("look") is False


def test_positive_input_case() -> None:
    assert is_isogram("playground") is True
