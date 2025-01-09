import pytest
from app.main import is_isogram


def test_case_insensitive_is_isogram() -> None:
    assert not is_isogram("AaAAAaaaa")


def test_empty_is_isogram() -> None:
    assert is_isogram("")


def test_non_consecutive_is_isogram() -> None:
    assert not is_isogram("acegikmoqsuwy")


def test_consecutive_is_isogram() -> None:
    assert not is_isogram("abcdefghijklmnopqrstuvwxyz")
