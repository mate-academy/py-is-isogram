from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") == True


def test_is_isogram1() -> None:
    assert is_isogram("look") == False


def test_is_isogram2() -> None:
    assert is_isogram("Adam") == False


def test_is_isogram3() -> None:
    assert is_isogram("") == True
