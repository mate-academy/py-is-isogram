import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("one", True),
        ("test", False),
        ("Test", False),
        ("miDdle", False),
        ("entEr", False),
        ("justice", True)
    ]
)
def test_isograms(
    word: int,
    result: bool
) -> None:
    assert (
        is_isogram(word) == result
    ), (f"{word} is an isogram - {result}")
