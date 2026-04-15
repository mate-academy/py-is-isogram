import pytest

from app.main import is_isogram

@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "test no repeating letters expected True",
        "test have repeating letters expected False",
        "test have repeating letters expected False",
        "test empty line, expected False"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result

