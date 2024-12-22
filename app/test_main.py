import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("Mark", (True)),
        ("playground", (True)),
        ("look", (False))
    ],
)
def test_for_words(
    word: str,
    expected: bool
) -> None:
    assert is_isogram(word) == expected
