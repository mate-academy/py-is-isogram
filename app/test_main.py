import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("player", True),
        ("monitor", False),
        ("bluetti", False),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("o", True),
        ("rOBOts", False),
        ("devELOP", False),
    ]
)
def test_is_isogram_positive(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
