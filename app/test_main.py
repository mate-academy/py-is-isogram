from app.main import is_isogram


def test_isogram_true() -> None:
    word = "playgrounds"

    result = is_isogram(word)

    assert result is True


def test_isogram_false_repeat_letters() -> None:
    word = "look"

    result = is_isogram(word)

    assert result is False


def test_isogram_case_insensitive() -> None:
    word = "Adam"

    result = is_isogram(word)

    assert result is False


def test_isogram_true_empty_string() -> None:
    word = ""

    result = is_isogram(word)

    assert result is True
