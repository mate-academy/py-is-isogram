from app.main import is_isogram
import pytest

@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("", True),
        ("   ", False),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Robert", False)
    ]
)
def test_cent_combination_valid(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result
