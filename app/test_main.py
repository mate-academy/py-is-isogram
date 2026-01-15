from app.main import is_isogram


def test_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_same_letters() -> None:
    assert is_isogram("look") is False


def test_case_letters() -> None:
    assert is_isogram("Adam") is False


def test_empty() -> None:
    assert is_isogram("") is True
