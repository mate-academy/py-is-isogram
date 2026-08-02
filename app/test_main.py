from app.main import is_isogram


def test_isogram_word() -> None:
    assert is_isogram("playgrounds")


def test_double_small_letters_in_word() -> None:
    assert not is_isogram("look")


def test_double_small_and_big_letters_in_word() -> None:
    assert not is_isogram("Adam")


def test_not_word() -> None:
    assert is_isogram("")
