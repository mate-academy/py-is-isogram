import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("a", True),
        ("aA", False),
        ("", True),
        ("playgrounds", True),
        ("Adam", False),
        ("John", True),
        ("AcBfglq", True)

    ],
    ids=[
        "one letter with lower case",
        "world short with Upper case",
        "zero string",
        "lower case letters do not repeat",
        "Upper case letters repeat",
        "Upper case letters do not repeat",
        "Mix case letters do not repeat"
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
