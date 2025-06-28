import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_function_has_or_no_similar_letters(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) is result


