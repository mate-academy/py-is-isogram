from app.main import is_isogram


def test_empty_input() -> None:
    assert is_isogram("") is True


def test_check() -> None:
    assert is_isogram("look") is False
    assert is_isogram("kola") is True
    assert is_isogram("focused") is True


def test_upper_lower_case_check() -> None:
    assert is_isogram("aA") is False
