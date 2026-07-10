from app import main


def test_playgrounds_is_isogram() -> None:
    assert main.is_isogram("playgrounds") is True


def test_look_is_not_isogram() -> None:
    assert main.is_isogram("look") is False


def test_adam_is_not_isogram_case_insensitive() -> None:
    assert main.is_isogram("Adam") is False


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True


def test_repeated_letters_non_consecutive() -> None:
    assert main.is_isogram("abca") is False


def test_case_insensitive_detection() -> None:
    assert main.is_isogram("aA") is False
