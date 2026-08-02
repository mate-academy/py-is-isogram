from app.main import is_isogram


def test_isogram_check_for_look_str() -> None:
    word = "look"
    result = is_isogram(word)

    assert result is False


def test_isogram_check_for_empty_str() -> None:
    word = ""
    result = is_isogram(word)

    assert result is True


def test_isogram_check_for_adam_str() -> None:
    word = "Adam"
    result = is_isogram(word)

    assert result is False


def test_isogram_check_for_playground_str() -> None:
    word = "playground"
    result = is_isogram(word)

    assert result is True
