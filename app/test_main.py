import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ]
)
def test_should_return_correct_answer(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
