from app.main import is_isogram


def test_should_return_true_when_word_is_empty() -> None:
    result = is_isogram("")

    assert result is True


def test_should_return_true_when_word_is_isogram() -> None:
    result = is_isogram("playgrounds")

    assert result is True


def test_should_return_false_when_word_is_non_isogram() -> None:
    result = is_isogram("look")

    assert result is False


def test_should_return_false_when_word_in_different_cases() -> None:
    result = is_isogram("Adam")

    assert result is False
