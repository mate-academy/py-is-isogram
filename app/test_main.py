
from app import main


def test_isogram() -> None:
    assert main.is_isogram("playgrounds") is True


def test_case_insensitive() -> None:
    assert main.is_isogram("aA") is False


def test_empty_string() -> None:
    assert main.is_isogram("") is True


def test_non_consecutive_letters() -> None:
    assert main.is_isogram("abca") is False


def test_consecutive_letters() -> None:
    assert main.is_isogram("aa") is False


def test_unique_letters() -> None:
    assert main.is_isogram("Python") is True
