from app.main import is_isogram


def test_is_isogram1() -> None:
    assert is_isogram("Hello") is False, "Should return False"


def test_is_isogram2() -> None:
    assert is_isogram("") is True, "Should return True"


def test_is_isogram3() -> None:
    assert is_isogram("Playgrounds") is True, "Should return True"


def test_is_isogram4() -> None:
    assert is_isogram("Amoeba") is False, "Should return False"
