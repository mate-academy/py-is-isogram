import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram_method_with_different_params(
        word: str,
        expected_result: bool
) -> None:
    assert (is_isogram(word) == expected_result), \
        f"is_isogram should return {expected_result}, when input is {word}"
