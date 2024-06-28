import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, is_true",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_modify_classes(word: str, is_true: bool) -> None:
    assert is_isogram(word) == is_true
