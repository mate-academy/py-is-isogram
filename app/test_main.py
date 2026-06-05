import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("sublime", True),
        ("Alpha", False),
        ("init", False),
        ("locksmith", True),
        ("hyperlink", True),
        ("complainer", True),
        ("Router", False),
        ("look", False),
        ("", True)
    ]
)
def test_function_finds_isograms_correctly(
    word: str, result: bool
) -> None:
    assert (is_isogram(word)) == result
