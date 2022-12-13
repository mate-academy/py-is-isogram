from app.main import is_isogram


def test_returns_true_if_empty_string() -> None:
    goals = is_isogram("")
    assert goals


def test_returns_true_if_no_repeating_letters() -> None:
    goals = is_isogram("glory")
    assert goals


def test_return_false_if_repeating_letters() -> None:
    goals = is_isogram("look")
    assert not goals


def test_function_is_case_insensitive() -> None:
    goals = is_isogram("Adam")
    assert not goals
