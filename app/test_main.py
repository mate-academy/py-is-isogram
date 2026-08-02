from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("", True),
        ("Adam", False),
    ]
)
def test_get_human_age(word: str,
                       expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
