from app.main import is_isogram


def test_is_isogram_should_return_true() -> None:
    assert (
        is_isogram("world") == True
    ), "test should check if the word is isogram"


def test_is_isogram_should_return_false() -> None:
    assert (
        is_isogram("assert") == False
    ), "test should return False if letter count is more than 1"


def test_is_isogram_should_be_case_insensitive() -> None:
    assert (
        is_isogram("helLo") == False
    ), "test should be case insensitive"


def test_when_string_empty() -> None:
    assert (
        is_isogram("") == True
    ), "empty string should return True"

def test_should_return_false_when_two_letters() -> None:
    assert (
        is_isogram("hipopotam") == False
    ), "should return False"
