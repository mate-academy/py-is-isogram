import pytest


from app.main import is_isogram


def test_should_return_true() -> None:
    word = ""
    parts = is_isogram(word)
    assert parts == True


def test_should_return_false() -> None:
    word = "look"
    parts = is_isogram(word)
    assert parts == False


def test_should_return_is_true1() -> None:
    word = "lads"
    parts = is_isogram(word)
    assert parts == True
