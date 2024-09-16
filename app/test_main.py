from app.main import is_isogram


def test_unique_word() -> None:
    assert is_isogram("playgrounds")


def test_repeated_letters() -> None:
    assert not is_isogram("look")


def test_non_unique_word() -> None:
    assert not is_isogram("Adam")


def test_just_a_string() -> None:
    assert is_isogram("")
