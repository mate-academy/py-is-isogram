import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("Adam", False),
        ("playgrounds", True),
        ("Look", False),
        ("uncopyrightable", True),
        ("dangerously", True),
        ("python", True),
        ("css", False)
    ]
)
def test_correct_isogram_determination(word: str, result: bool) -> None:
    assert is_isogram(word) == result
