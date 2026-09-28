from app.main import is_isogram


def test_letters_no_repeat() -> None:
    assert is_isogram("playgrounds")


def test_letters_repeat() -> None:
    assert not is_isogram("look")


def test_letters_no_upper_and_lower() -> None:
    assert not is_isogram("Adam")


def test_letters_empty() -> None:
    assert is_isogram("")
