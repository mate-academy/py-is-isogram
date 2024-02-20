import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_word,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("NASA", False),
        ("USA", True),
        ("a", True),
        ("aa", False),
        ("Uncopyrightable", True),
        ("Algorithmization", False)
    ]
)
def test_is_isogram(
        input_word: str,
        expected_result: bool
) -> None:
    assert is_isogram(input_word) == expected_result
