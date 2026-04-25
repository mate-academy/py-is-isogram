from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("isogram", True),
        ("sixyearold", True),

        ("alphabet", False),
        ("programming", False),

        ("Dermatoglyphics", True),
        ("abA", False),
        ("moOse", False), ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        None,
        123,
        ["abc"],
        {"a": 1},
    ],
    ids=[
        "none",
        "int",
        "list",
        "dict",
    ]
)
def test_is_isogram_invalid_types(word: str) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)
