from app.main import is_isogram


def test_different_letters() -> None:
    isogram = "playgrounds"
    result = is_isogram(isogram)
    assert result is True


def test_big_and_small_letter() -> None:
    isogram = "Adam"
    result = is_isogram(isogram)
    assert result is False


def test_empty_string() -> None:
    isogram = ""
    result = is_isogram(isogram)
    assert result is True


def test_small_different() -> None:
    isogram = "look"
    result = is_isogram(isogram)
    assert result is False
