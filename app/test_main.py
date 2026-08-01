from app.main import is_isogram


def test_empty_word() -> None:
    goals = is_isogram("")
    assert goals is True


def test_isogram_word() -> None:
    goals = is_isogram("look")
    assert goals is False


def test_isogram_uppercase_word() -> None:
    goals = is_isogram("Adam")
    assert goals is False


def test_not_isogram_word() -> None:
    goals = is_isogram("playground")
    assert goals is True
