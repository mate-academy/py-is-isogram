import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, return_value",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ],
    ids=[
        "Test check result value if word equal to empty string",
        "Test check result value if word contains only unique characters",
        "Test check result value if word contains same characters",
        "Test check result if word contains same characters in different case"
    ]
)
def test_check_is_isogram_that_are_returned(
        word: str,
        return_value: bool
) -> None:
    assert (is_isogram(word) == return_value), \
        (f"For characters set \'{word}\' "
         f"returned value should be equal to {return_value}")


@pytest.mark.parametrize(
    "word, expected_error",
    [
        (6, TypeError),
        (3.5, TypeError),
        (None, TypeError),
        ([5], TypeError),
        ({16}, TypeError)
    ],
    ids=[
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data",
        "Should raise error if input incorrect type of input data"
    ]
)
def test_raising_errors(
        word: str,
        expected_error: TypeError
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
