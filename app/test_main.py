from app.main import is_isogram


def test_isogram_true() -> None:
    assert is_isogram("playgrounds")


def test_isogram_false() -> None:
    assert not is_isogram("look")


def test_case_sensitive() -> None:
    assert not is_isogram("Adam")


def test_empty() -> None:
    assert is_isogram("")
