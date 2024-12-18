import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("playgrounds", True),
        ("letter", False),
        ("bOok", False),
        ("tests", False)
    ]
)
def test_check_is_word_isogram(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) is result
