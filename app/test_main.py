from app.main import is_isogram


def test_one() -> None:
    assert is_isogram("playgrounds") is True


def test_two() -> None:
    assert is_isogram("look") is False


def test_three() -> None:
    assert is_isogram("Adam") is False


def test_for_empty_str() -> None:
    assert is_isogram("") is True
