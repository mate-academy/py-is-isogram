import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, bool_meaning",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_function(
        word: str,
        bool_meaning: bool
) -> None:
    assert is_isogram(word) == bool_meaning
