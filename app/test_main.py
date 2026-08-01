import pytest
from string import ascii_lowercase, ascii_uppercase

from app.main import is_isogram


@pytest.mark.parametrize("string", [
    "ands", "aavgje", "Aweka"
])
def test_func_should_return_bool(
        string: str
) -> None:
    assert isinstance(is_isogram(string), bool)


@pytest.mark.parametrize("string, expected", [
    ("abc", True),
    ("aabc", False),
    (ascii_lowercase, True),
    (ascii_lowercase + "a", False),
    ("", True)
])
def test_func_should_return_correct_result(
        string: str,
        expected: bool
) -> None:
    actual = is_isogram(string)
    assert actual == expected


@pytest.mark.parametrize("string, expected", [
    ("AbC", True),
    ("Aabc", False),
    (ascii_uppercase, True),
    (ascii_uppercase + "a", False)
])
def test_func_should_return_correct_result_with_uppercase(
        string: str,
        expected: bool
) -> None:
    actual = is_isogram(string)
    assert actual == expected

# test_func_should_return_correct_result_with_punctuation
