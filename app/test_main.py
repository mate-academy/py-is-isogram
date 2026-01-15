from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_string_diff_case() -> None:
    assert is_isogram("look") is False


def test_big_letters() -> None:
    assert is_isogram("Adam") is False
