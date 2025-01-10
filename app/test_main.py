from app.main import is_isogram


def test_check_letters() -> None:
    assert is_isogram("playgrounds")


def test_fail() -> None:
    assert not is_isogram("look")


def test_register() -> None:
    assert not is_isogram("Adam")


def test_none() -> None:
    assert is_isogram("")
