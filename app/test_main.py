from app.main import is_isogram


def test_is_empty_str() -> None:
    isogram = is_isogram("")

    assert isogram is True


def test_is_lower_case() -> None:
    isogram = is_isogram("look")

    assert isogram is False


def test_is_upper_case() -> None:
    isogram = is_isogram("Adam")

    assert isogram is False


def test_is_non_repeated_letters() -> None:
    isogram = is_isogram("playgrounds")

    assert isogram is True
