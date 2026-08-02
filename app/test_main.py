from app.main import is_isogram


def test_should_return_bool() -> None:
    is_bool = is_isogram("playgrounds")
    assert isinstance(is_bool, bool)


def test_two_letters_extra() -> None:
    empty = is_isogram("Adam")
    assert empty is False


def test_g() -> None:
    result = is_isogram("Playgrounds")
    assert result is True


def test_empty_string() -> None:
    empty = is_isogram("")
    assert empty is True


def test_two_letters_together() -> None:
    result = is_isogram("look")
    assert result is False
