from app import main


def test_empty_string() -> None:
    assert main.is_isogram("") is True


def test_isogram_true() -> None:
    assert main.is_isogram("playgrounds") is True
    assert main.is_isogram("subdermatoglyphic") is True


def test_consecutive_letters_false() -> None:
    assert main.is_isogram("look") is False
    assert main.is_isogram("aa") is False


def test_non_consecutive_letters_false() -> None:
    assert main.is_isogram("aba") is False
    assert main.is_isogram("alphabet") is False


def test_case_insensitivity() -> None:
    assert main.is_isogram("Adam") is False
    assert main.is_isogram("Aa") is False
    assert main.is_isogram("mMo") is False
