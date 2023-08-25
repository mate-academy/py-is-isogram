from app.main import is_isogram

import pytest


def test_should_accept_empty_string() -> None:
    assert is_isogram("") is True


def test_should_reject_consecutive_isograms() -> None:
    assert is_isogram("doll") is False


def test_should_reject_non_consecutive_isograms() -> None:
    assert is_isogram("lol") is False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("hapPy") is False


def test_should_return_true_when_isogram() -> None:
    assert is_isogram("wonderful") is True
