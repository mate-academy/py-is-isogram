from app.main import is_isogram


def test_check_for_empty_str() -> None:
    word = ""
    expected = is_isogram(word)

    assert expected is True


def test_check_for_look_str() -> None:
    word = "look"
    expected = is_isogram(word)

    assert expected is False


def test_check_for_adam_str() -> None:
    word = "Adam"
    expected = is_isogram(word)

    assert expected is False


def test_check_for_playground_str() -> None:
    word = "playground"
    expected = is_isogram(word)

    assert expected is True
