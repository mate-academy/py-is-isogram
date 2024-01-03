from app.main import is_isogram


def test_1() -> None:
    assert is_isogram("playgrounds") is True, "test 1"


def test_2() -> None:
    assert is_isogram("look") is False, "test 2"


def test_3() -> None:
    assert is_isogram("Adam") is False, "test 3"


def test_4() -> None:
    assert is_isogram("") is True, "test 4"
