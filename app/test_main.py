import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("Mark", True),
        ("mark", True),
        ("Test", False),
        ("test", False)
    ]
)
def test_function_should_be_case_insensitive(word, expected):
    assert is_isogram(word) == expected


def test_empty_string_should_be_isogram():
    assert is_isogram("")


def test_consecutive_letters_are_not_isogram():
    assert not is_isogram("tees")


def test_non_consecutive_letters_are_not_isogram():
    assert not is_isogram("test")
