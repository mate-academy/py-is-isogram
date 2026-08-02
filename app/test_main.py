import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("hello", False),
        ("look", False),
        ("world", True),
        ("playground", True),
        ("Adam", False),
        ("alphabet", False),
        ("playgrounds", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_is_isogram_empty() -> None:
    assert is_isogram("") is True
