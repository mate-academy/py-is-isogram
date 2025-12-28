from app.main import is_isogram


def test_word_with_different_letters() -> None:
    goals = is_isogram("playgrounds")
    assert goals is True


def test_word_with_same_letters() -> None:
    goals = is_isogram("look")
    assert goals is False


def test_word_with_high_register() -> None:
    goals = is_isogram("Adam")
    assert goals is False


def test_with_empty_line() -> None:
    goals = is_isogram("")
    assert goals is True
