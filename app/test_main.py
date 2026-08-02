import pytest

from typing import Any
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("plAyGroUnds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_return_correct_bool(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word,exception",
    [
        (5, AttributeError),
        (["look", "rea"], AttributeError),
        ((5, "perf"), AttributeError),
    ]
)
def test_word_must_be_str(word: Any, exception: type[Exception]) -> None:
    with pytest.raises(exception):
        is_isogram(word)
