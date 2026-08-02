from app.main import is_isogram


def test_true_for_empty_string() -> None:
    word = ""

    result = is_isogram(word)

    assert result is True


def test_true_for_string_playgrounds() -> None:
    word = "Playgrounds"

    result = is_isogram(word)

    assert result is True


def test_false_for_string_look() -> None:
    word = "look"

    result = is_isogram(word)

    assert result is False


def test_false_for_string_adam() -> None:
    word = "Adam"

    result = is_isogram(word)

    assert result is False
