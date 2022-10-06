from app.main import is_isogram


def test_empty_string() -> None:
    word = is_isogram("")

    assert word is True


def test_consecutive_same_letters() -> None:
    word = is_isogram("loOk")

    assert word is False


def test_non_consecutive_same_letters() -> None:
    word = is_isogram("Adam")

    assert word is False


def test_isogram_word() -> None:
    word = is_isogram("playGrounds")

    assert word is True