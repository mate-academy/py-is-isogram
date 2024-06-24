from app.main import is_isogram


def test_is_isogram_first() -> None:
    assert is_isogram("playgrounds") == True, "That string is isogram"


def test_is_isogram_second() -> None:
    assert is_isogram("look") == False, "That string is not isogram"


def test_is_isogram_third() -> None:
    assert is_isogram("Adam") == False, "That string is not isogram"


def test_is_isogram_fourth() -> None:
    assert is_isogram("") == True, "That string is isogram"
