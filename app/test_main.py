import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "testing_word, expected",
    [
        ("playgrounds", True),
        ("book", False),
        ("", True),
        ("Bob", False),
    ]
)
def test_is_isogram(testing_word: str, expected: bool) -> None:
    assert is_isogram(testing_word) == expected
