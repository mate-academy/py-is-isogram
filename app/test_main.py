from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_case_insensetive() -> None:
    assert is_isogram("Wow") is False
    assert is_isogram("wow") is False


def test_isogram() -> None:
    assert is_isogram("playground") is True
    assert is_isogram("look") is False
