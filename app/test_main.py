from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("Welcome", False),
        ("Hello", False),
        ("name", True),
        ("", True),
        ("Elocvent", False),
        ("qwertyuiop", True)
    ]
)
def test_if_works(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_wrong_type() -> None:
    with pytest.raises(TypeError):
        is_isogram(5.785)
