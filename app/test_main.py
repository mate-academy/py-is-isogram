import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("", True),
    ("a", True),
    ("playgrounds", True),
    ("look", False),
    ("ABBA", False),
    ("ABba", False),
    ("PinkFloyd", True),
    ("RoyalBld", False)
])
def test_should_return_expected_results(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected
