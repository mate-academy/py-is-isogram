from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("")


def test_consecutive_same_letters() -> None:
    assert not is_isogram("look")


def test_non_consecutive_same_letters() -> None:
    assert not is_isogram("Adam")


def test_isogram_word() -> None:
    assert is_isogram("playgrounds")
