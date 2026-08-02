from app.main import is_isogram


def test_word_starts_with_upper() -> None:
    result = is_isogram("Adam")
    assert result is False


def test_empty_string() -> None:
    result = is_isogram("")
    assert result is True


def test_word_with_same_letters() -> None:
    result = is_isogram("look")
    assert result is False
