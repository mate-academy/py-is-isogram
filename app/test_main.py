import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("ABCDEFGHIJKLMNO", True),
        ("abcdefghijklmno", True),
        ("ala", False),
        ("ALA", False),
        ("Ala", False),
        ("", True),


    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_for_not_string() -> None:
    with pytest.raises(TypeError):
        is_isogram(1)
