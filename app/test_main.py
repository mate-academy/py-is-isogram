import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("isogram", True),
    ],
    ids=[
        "empty_string",
        "single_letter",
        "playgrounds_true",
        "look_false",
        "Adam_false",
        "isogram_true",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
