import pytest
from app.main import is_isogram


def test_check_type_return_is_bool() -> None:
    assert isinstance(is_isogram("Maksim"), bool)


def test_check_should_be_case_insensitive_up_register() -> None:
    assert is_isogram(word="MAKSI") == True


def test_check_is_empty_argument_return_true() -> None:
    assert is_isogram(word="") == True


def test_check_arguments_with_different_cases() -> None:
    assert is_isogram(word="Maksim") == False


def test_check_argument_with_same_latter_is_false() -> None:
    assert is_isogram(word="abrakadabra") == False

