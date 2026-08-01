import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("playgrounds", True),
        ("llama", False),
        ("Mermaid", False),
        ("moom", False),
    ]
)
def test_word_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
