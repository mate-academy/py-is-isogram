from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word , expected",
    [
        ("GemoGrapHic", True),
        ("adam", False),
        ("bankruptcy", True),
        ("", True),
        ("gagarin", False),
        ("GaGarIn", False),
        ("look", False)
    ]
)
def test_word_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
