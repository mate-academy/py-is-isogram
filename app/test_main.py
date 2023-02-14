import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]

)
def test_should_return(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected
