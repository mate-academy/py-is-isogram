from app.main import is_isogram


def test_normal_function_running_with_isogram() -> None:
    assert is_isogram("isogram T_ue") is True


def test_normal_function_running_with_not_isogram() -> None:
    assert is_isogram("not isogrAm False") is False


def test_empty_string_must_return_true() -> None:
    assert is_isogram("") is True


def test_single_space_string_must_return_true() -> None:
    assert is_isogram(" ") is True


def test_double_space_string_must_return_false() -> None:
    assert is_isogram("  ") is False


def test_function_must_be_case_insensitive() -> None:
    assert is_isogram("aA") is False
