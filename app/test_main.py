from app import main
import pytest


@pytest.mark.parametrize(
    "word , expected",
    [
        ("DemoGrapHic", True),
        ("adam", False),
        ("bankruptcy", True),
        ("", True),
        ("gagarin", False),
        ("GagArIn", False),
        ("look", False)
    ]
)
def test_word_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected
