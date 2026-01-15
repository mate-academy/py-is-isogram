from app import main


def test_isogram_with_unique_letters() -> None:
    assert main.is_isogram("playgrounds") is True
    assert main.is_isogram("abcdefg") is True
    assert main.is_isogram("zyx") is True


def test_isogram_with_repeating_letters() -> None:
    assert main.is_isogram("look") is False
    assert main.is_isogram("Adam") is False
    assert main.is_isogram("hello") is False
    assert main.is_isogram("aabbcc") is False


def test_isogram_with_mixed_case() -> None:
    assert main.is_isogram("PlayGrounds") is True
    assert main.is_isogram("Look") is False
    assert main.is_isogram("Adam") is False
    assert main.is_isogram("HeLLo") is False


def test_isogram_with_empty_string() -> None:
    assert main.is_isogram("") is True


def test_isogram_with_single_character() -> None:
    assert main.is_isogram("a") is True
    assert main.is_isogram("A") is True
