import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "value,expectation",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "test_should_return_true_when_value_do_not_repeated_letter",
        "test_should_return_false_when_value_repeated_letter_in_same_case",
        "test_should_return_false_when_value_repeated_letter_different_case",
        "test_should_return_true_when_value_is_empty"
    ]
)
def test_is_isogram(
        value: str,
        expectation: bool
) -> None:
    assert is_isogram(value) == expectation
