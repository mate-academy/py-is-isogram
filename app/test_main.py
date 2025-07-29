from app.main import is_isogram


def test_if_string_is_empty() -> None:
    assert is_isogram("")


def test_if_string_is_isogram() -> None:
    assert is_isogram("playgrounds")


def test_if_string_is_not_isogram() -> None:
    assert not is_isogram("look")


def test_if_string_starts_from_title_letter() -> None:
    assert not is_isogram("Adam")
