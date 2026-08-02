import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("abc", True),
        ("Aabc", False),
        ("aabc", False),
        ("abac", False)
    ]
)
def test_boundaries(word: str, result: bool) -> None:
    assert is_isogram(word) == result


def test_type_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(1)
