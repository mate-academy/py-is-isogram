import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word_to_test, expected_bool_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram_function(
        word_to_test: str,
        expected_bool_result: bool
) -> None:
    assert is_isogram(word_to_test) == expected_bool_result
