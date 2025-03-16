import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,isogram",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Madam", False)
    ]
)
def test_is_the_isogram_check_correct(
    word: str,
    isogram: bool
) -> None:
    assert is_isogram(word) == isogram
