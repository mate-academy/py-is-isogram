from app.main import is_isogram


def test_word_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_word_is_name() -> None:
    assert is_isogram("Adam") is False


def test_word_is_empty() -> None:
    assert is_isogram("") is True
