from app.main import is_isogram


def test_1() -> None:
    assert is_isogram("playgrounds") is True


def test_2() -> None:
    assert is_isogram("look") is False


def test_3() -> None:
    assert is_isogram("Adam") is False


def test_4() -> None:
    assert is_isogram("") is True
