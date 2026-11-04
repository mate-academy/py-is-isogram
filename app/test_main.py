from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("lumberjacks", True),
        ("background", True),
        ("downstream", True),
        ("isogram", True),
        ("thumbscrew", True),
        ("AbA", False),
        ("IsOgRaM", True),
        ("MoOsE", False),
        ("aba", False),
        ("moose", False),
        ("alphabet", False),
        ("repetitive", False),
        ("", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
