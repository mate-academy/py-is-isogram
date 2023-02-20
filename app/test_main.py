from app.main import is_isogram


def test_with_empty_string() -> None:
    assert is_isogram("") is True


def test_with_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_with_non_repeating_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_with_mixed_case_letters() -> None:
    assert is_isogram("Adam") is False


def test_with_all_capital_letters() -> None:
    assert is_isogram("PYTHON") is True
