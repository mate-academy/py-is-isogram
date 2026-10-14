import pytest
from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),

    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    # Виклик змінено на main.get_coin_combination
    assert main.is_isogram(word) == expected, (
        f"Expected {expected} for word {word}"
    )
