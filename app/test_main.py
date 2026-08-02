from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_case_1() -> None:
    assert is_isogram("playgrounds") is True


def test_case_2() -> None:
    assert is_isogram("look") is False


def test_case_3() -> None:
    assert is_isogram("Adam") is False
