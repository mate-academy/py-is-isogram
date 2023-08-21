import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("PlAyGrOuNdS", True),
        ("look", False),
        ("RESULTe", False),
        ("wORd", True),
        ("", True),
        ("ambidextrously", True),
        ("UnCopyRightable", True)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
