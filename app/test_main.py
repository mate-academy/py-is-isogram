import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "word in lower",
        "word in lower with repetition",
        "word in upper with repetition",
        "empty line"
    ]
)
def test_should_return_bool_if_word_is_isogram(word: str,
                                               result: bool) -> None:
    assert is_isogram(word) == result
