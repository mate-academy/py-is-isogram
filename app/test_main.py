from app.main import is_isogram


def test_is_isogram_1() -> None:
    result = is_isogram("playgrounds")
    assert result is True


def test_is_isogram_2() -> None:
    result = is_isogram("look")
    assert result is False


def test_is_isogram_3() -> None:
    result = is_isogram("Adam")
    assert result is False


def test_is_isogram_4() -> None:
    result = is_isogram("")
    assert result is True
