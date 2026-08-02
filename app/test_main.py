import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, isogram",
    [
        ("", True),
        ("Alex", True),
        ("TabLe", True),
        ("Lama", False),
        ("PhIloSophy", False),
        ("plaYgrOunDs", True),
        ("moon", False),
        ("Aaron", False)
    ]
)
def test_isogram(
        word: str,
        isogram: bool
) -> None:
    assert is_isogram(word) == isogram
