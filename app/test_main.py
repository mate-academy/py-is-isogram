import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "testing_input, expected_output",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Look", False),
        ("adam", False),
        ("Adam", False),
        ("Abcd", True)
    ]
)
def test_is_isogram(
        testing_input: str,
        expected_output: bool
) -> None:
    assert is_isogram(testing_input) == expected_output
