from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("AdamM", False),
        ("", True),
        ("Adidas", False),
    ],
    ids=[
        "word 'playgrounds' must return 'True'",
        "word 'look' must return 'False'",
        "word 'AdamM' must return 'False'",
        "word '' must return 'True'",
        "word 'Adidas' must return 'False'"
    ]
)
def test_should_return_correct_result(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
