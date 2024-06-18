from app.main import is_isogram


def test_empty_string() -> None:
    word = is_isogram("")
    assert word is True


def test_word_with_doubled_letters() -> None:
    word = is_isogram("look")
    assert word is False


def test_word_without_doubled_letters() -> None:
    word = is_isogram("playgrounds")
    assert word is True


def test_word_another_type() -> None:
    word = is_isogram("5")
    assert word is False
