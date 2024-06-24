from app.main import is_isogram


def test_is_histogram_first() -> None:
    assert is_isogram("playgrounds"), "That string is histogram"


def test_is_histogram_second() -> None:
    assert not is_isogram("look"), "That string is not histogram"


def test_is_histogram_third() -> None:
    assert not is_isogram("Adam"), "That string is not histogram"


def test_is_histogram_fourth() -> None:
    assert is_isogram(""), "That string is histogram"
