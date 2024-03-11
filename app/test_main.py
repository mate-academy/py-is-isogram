import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("word", True),
        ("result", True),
        ("", True),
        ("False", True),
        ("pytest", False),
        ("parametrize", False),
        ("Anagram", False),
        ("cool", False),
        ("Aaron", False)
    ]
)
def test_for_correct_results(word: str, result: bool) -> None:
    assert is_isogram(word) == result
